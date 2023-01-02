from containsNoCapacitors import *
from getFinalComponent import *
from findRoadsWithOutCapacitors import *
from allInSeries import *
from findReconnection import *
from systemCapacitanceCalcNotInclusive import *
from systemCapacitanceCalcFrontInclusive import *
from getNewComponents import *

# Assigns voltages to each component as necessary.
# For Capacitors this is based on the current time.
# For Resistors this is based on Ohms Law: V = IR
# Yes, there is a lot of long lines of code here, however I believe that it makes
# it the most understandable it can be.
def voltageAssignment(powerNode, graph, components, time, totalCapacitance, systemVoltage):
    if containsNoCapacitors(components):
        for component in components:
            componentVoltage = component.getResistance() * component.getCurrent()
            component.setVoltage(componentVoltage)
    else:
        if time == 0:
            for component in components:
                if not isinstance(component, Capacitor):
                    componentVoltage = component.getResistance() * component.getCurrent()
                    component.setVoltage(componentVoltage)
                else:
                    component.setVoltage(0)
        else:
            startingComponent = powerNode.getComponent()
            endComponent = getFinalComponent(graph)
            graphWithOutCapacitors = findRoadsWithOutCapacitors(startingComponent, 
                                                                graph, endComponent)
            if graphWithOutCapacitors == None:
                if allInSeries(graph):
                    for component in components:
                        if not isinstance(component, Capacitor):
                            component.setVoltage(0)
                        else:
                            capacitorVoltage = (systemVoltage) * (totalCapacitance / component.getCapacitance())
                            component.setVoltage(capacitorVoltage)
                else:
                    currentComponent = startingComponent
                    pathVoltage = systemVoltage
                    pathTotalCapacitance = totalCapacitance
                    while currentComponent != endComponent:

                        if isinstance(currentComponent, Capacitor):
                            capacitorVoltage = (pathVoltage) * (pathTotalCapacitance / currentComponent.getCapacitance())
                            currentComponent.setVoltage(capacitorVoltage)
                        else:
                            currentComponent.setVoltage(0)

                        if len(graph[currentComponent]) == 1:
                            currentComponent = graph[currentComponent][0]
                        else:
                            reconnectionComponent = findReconnection(graph, currentComponent, endComponent)
                            parallelSubSystemTotalCapacitance = systemCapacitanceCalcNotInclusive(currentComponent, graph, reconnectionComponent)
                            if parallelSubSystemTotalCapacitance != 0:
                                newPathVoltage = (pathVoltage) * (pathTotalCapacitance / parallelSubSystemTotalCapacitance)
                            else:
                                newPathVoltage = 0
                            for subComponent in graph[currentComponent]:
                                component = subComponent
                                seriesSubSystemTotalCapacitance = systemCapacitanceCalcFrontInclusive(subComponent, graph, reconnectionComponent)
                                while component != reconnectionComponent:
                                    if isinstance(component, Capacitor):
                                        capacitorVoltage = (newPathVoltage) * (seriesSubSystemTotalCapacitance / component.getCapacitance())
                                    else:
                                        capacitorVoltage = 0
                                    component.setVoltage(capacitorVoltage)
                                    # assuming series case here could change in future
                                    component = graph[component][0]

                            currentComponent = reconnectionComponent
                    if isinstance(endComponent, Capacitor):
                        capacitorVoltage = (pathVoltage) * (pathTotalCapacitance / endComponent.getCapacitance())
                        endComponent.setVoltage(capacitorVoltage)
                    else:
                        endComponent.setVoltage(0)

            # There is a path without Capacitors
            else:
                # Deal with resistors
                capacitorFreeComponents = getNewComponents(graphWithOutCapacitors)
                for component in capacitorFreeComponents:
                    componentVoltage = component.getResistance() * component.getCurrent()
                    component.setVoltage(componentVoltage)

                # Deal with capacitors
                currentComponent = startingComponent
                pathVoltage = systemVoltage
                pathTotalCapacitance = totalCapacitance
                while currentComponent != endComponent:

                    if isinstance(currentComponent, Capacitor):
                        capacitorVoltage = (pathVoltage) * (pathTotalCapacitance / currentComponent.getCapacitance())
                        component.setVoltage(capacitorVoltage)

                    if len(graph[currentComponent]) == 1:
                        currentComponent = graph[currentComponent][0]
                    else:
                        reconnectionComponent = findReconnection(graph, currentComponent, endComponent)
                        parallelSubSystemTotalCapacitance = systemCapacitanceCalcNotInclusive(currentComponent, graph, reconnectionComponent)
                        if parallelSubSystemTotalCapacitance != 0:
                            newPathVoltage = (pathVoltage) * (pathTotalCapacitance / parallelSubSystemTotalCapacitance)
                        else:
                            pass
                        for subComponent in graph[currentComponent]:
                            component = subComponent
                            seriesSubSystemTotalCapacitance = systemCapacitanceCalcFrontInclusive(subComponent, graph, reconnectionComponent)
                            while component != reconnectionComponent:
                                if isinstance(component, Capacitor):
                                    capacitorVoltage = (newPathVoltage) * (seriesSubSystemTotalCapacitance / component.getCapacitance())
                                    component.setVoltage(capacitorVoltage)
                                else:
                                    componentVoltage = component.getCurrent() * component.getResistance()
                                    component.setVoltage(componentVoltage)
                                # assuming series case here could change in future
                                component = graph[component][0]

                        currentComponent = reconnectionComponent

                # Deal with resistors
                capacitorFreeComponents = getNewComponents(graphWithOutCapacitors)
                for component in capacitorFreeComponents:
                    componentVoltage = component.getResistance() * component.getCurrent()
                    component.setVoltage(componentVoltage)