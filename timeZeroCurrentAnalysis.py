from allInSeries import *
from getFinalComponent import *
from findReconnection import *
from subDataCreater import *
from containsNoCapacitors import *
from parallelResistanceCalc import *
from parallelResistanceCalcWithCapacitors import *
from systemCapacitanceCalcNotInclusive import *
from systemCapacitanceCalcFrontInclusive import *

# Performs the current anaylsis of a system that should be at 0 tao.
# This means that the capacitors are not charged and therefore full current runs
# over them and not resistors.
def timeZeroCurrentAnalysis(powerNode, graph, components, systemCurrent):
    if allInSeries(graph):
        for component in components:
            component.setCurrent(systemCurrent)
    else:
        startingComponent = powerNode.getComponent()
        startingComponent.setCurrent(systemCurrent)
        endComponent = getFinalComponent(graph)
        endComponent.setCurrent(systemCurrent)
        currentComponent = startingComponent
        while currentComponent != endComponent:
            if len(graph[currentComponent]) == 1:
                nextComponent = graph[currentComponent][0]
                nextComponent.setCurrent(currentComponent.getCurrent())
                currentComponent = nextComponent
            else:
                reconnectionComponent = findReconnection(graph, currentComponent, endComponent)
                subDataStructure = subDataCreater(graph, currentComponent, reconnectionComponent)
                chainIndex = len(subDataStructure) - 1
                while chainIndex >= 0:
                    if containsNoCapacitors(subDataStructure[chainIndex]):
                        for component in subDataStructure[chainIndex]:
                            component.setCurrent(0)
                        subDataStructure.pop(chainIndex)
                    chainIndex -= 1
                if subDataStructure == []:
                    parallelResistance = parallelResistanceCalc(graph, currentComponent, reconnectionComponent)
                    parallelVoltage = systemCurrent * parallelResistance
                    for resistor in graph[currentComponent]:
                        resistanceSum = 0
                        resistorPassOne = resistor
                        resistorPassTwo = resistor
                        while resistorPassOne != reconnectionComponent:
                            resistanceSum += resistorPassOne.getResistance()
                            nextResistor = graph[resistorPassOne][0]
                            resistorPassOne = nextResistor
                        pathCurrent = parallelVoltage / resistanceSum
                        while resistorPassTwo != reconnectionComponent:
                            resistorPassTwo.setCurrent(pathCurrent)
                            nextResistor = graph[resistorPassTwo][0]
                            resistorPassTwo = nextResistor
                    currentComponent = reconnectionComponent
                    reconnectionComponent.setCurrent(systemCurrent)
                else:
                    parallelResistance = parallelResistanceCalcWithCapacitors(subDataStructure)
                    parallelVoltage = systemCurrent * parallelResistance
                    for component in graph[currentComponent]:
                        resistanceSum = 0
                        componentPassOne = component
                        componentPassTwo = component
                        while componentPassOne != reconnectionComponent:
                            if not isinstance(componentPassOne, Capacitor):
                                resistanceSum += componentPassOne.getResistance()
                            nextComponent = graph[componentPassOne][0]
                            componentPassOne = nextComponent
                        if resistanceSum != 0:
                            pathCurrent = parallelVoltage / resistanceSum
                        else:
                            parallelSubSystemTotalCapacitance = systemCapacitanceCalcNotInclusive(currentComponent, graph, reconnectionComponent)
                            seriesSubSystemTotalCapacitance = systemCapacitanceCalcFrontInclusive(component, graph, reconnectionComponent)
                            pathCurrent = (systemCurrent) * (seriesSubSystemTotalCapacitance / parallelSubSystemTotalCapacitance)
                        while componentPassTwo != reconnectionComponent:
                            for chain in subDataStructure:
                                if componentPassTwo in chain:
                                    componentPassTwo.setCurrent(pathCurrent)
                            nextComponent = graph[componentPassTwo][0]
                            componentPassTwo = nextComponent
                    currentComponent = reconnectionComponent
                    reconnectionComponent.setCurrent(systemCurrent)