from allInSeries import *
from getFinalComponent import *
from findRoadsWithOutCapacitors import *
from totalResistanceCalcNoCapacitors import *
from getNewComponents import *
from resistorOnlyCurrentAnalysis import *

# Performs the current anaylsis of a system that should be at 5 tao.
# This means that the capacitors have been fully charged and therefore no
# current runs over them.
def timeFiveTaoCurrentAnalysis(powerNode, graph, components):
    if allInSeries(graph):
        for component in components:
            component.setCurrent(0)
    else:
        startingComponent = powerNode.getComponent()
        endComponent = getFinalComponent(graph)
        graphWithOutCapacitors = findRoadsWithOutCapacitors(startingComponent, 
                                                            graph, 
                                                            endComponent)
        if graphWithOutCapacitors == None:
            for component in components:
                component.setCurrent(0)
        else:
            for component in components:
                if component not in graphWithOutCapacitors:
                    component.setCurrent(0)
            newTotalResistance = totalResistanceCalcNoCapacitors(powerNode, 
                                                                 graphWithOutCapacitors)
            systemVoltage = powerNode.getVoltage()
            newSystemCurrent = systemVoltage / newTotalResistance
            newComponents = getNewComponents(graphWithOutCapacitors)
            resistorOnlyCurrentAnalysis(powerNode, graphWithOutCapacitors, 
                                        newComponents, newSystemCurrent)
