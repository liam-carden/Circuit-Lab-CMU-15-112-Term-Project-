from containsPowerNode import *
from containsGroundNode import *
from containsNoCapacitors import *
from calcI import *
from orderComponents import *
from createDataStructure import *
from currentAnalysis import *
from totalResistanceCalc import *
from totalCapacitanceCalc import *
from voltageAssignment import *

# runs a complete analysis of the circuit
def runAnalysis(app, components, time):

    # few error out cases
    if components == []:
        return "Draw a Circuit"
    if not containsPowerNode(components):
        return "This circuit is not connected to power, please redesign"
    elif not containsGroundNode(components):
        return "This circuit is not connected to ground, please redesign"

    # assigns the powerNode and powerComponent
    for component in components:
        if component.isPowerComponent():
            powerComponent = component
            powerNode = powerComponent.getPowerNode()

    orderComponents(powerNode)
    app.graph = createDataStructure(powerNode)
    graph = app.graph

    # ensure the circuit is not incomplete
    for key in graph:
        if len(graph[key]) == 0:
            return "Incomplete Circuit"

    totalResistance = totalResistanceCalc(powerNode, graph, components, time)
    app.totalResistance = totalResistance

    if containsNoCapacitors(components):
        totalCapacitance = 0
    else:
        totalCapacitance = totalCapacitanceCalc(powerNode, graph)
    
    app.totalCapacitance = totalCapacitance

    systemVoltage = powerNode.getVoltage()
    app.circuitVoltage = systemVoltage

    systemCurrent = calcI(systemVoltage, totalResistance)
    app.circuitCurrent = systemCurrent

    currentAnalysis(powerNode, graph, components, time, systemCurrent)

    voltageAssignment(powerNode, graph, components, time, totalCapacitance, systemVoltage)

    return "Analysis Complete"