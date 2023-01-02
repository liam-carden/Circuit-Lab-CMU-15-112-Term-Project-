from allInSeries import *
from getFinalComponent import *
from findReconnection import *
from parallelResistanceCalc import *

# preforms a complete current anaylsis of the circuit via the graph
# data structure. Only works if the circuit does not contain any capacitors
def resistorOnlyCurrentAnalysis(powerNode, graph, components, systemCurrent):
    if allInSeries(graph):
        for resistor in components:
            resistor.setCurrent(systemCurrent)
    else:
        startingResistor = powerNode.getComponent()
        startingResistor.setCurrent(systemCurrent)
        endResistor = getFinalComponent(graph)
        endResistor.setCurrent(systemCurrent)
        currentResistor = startingResistor
        while currentResistor != endResistor:
            if len(graph[currentResistor]) == 1:
                nextResistor = graph[currentResistor][0]
                nextResistor.setCurrent(currentResistor.getCurrent())
                currentResistor = nextResistor
            else:
                reconnectionResistor = findReconnection(graph, currentResistor, endResistor)
                totalMiniParallelResistance = parallelResistanceCalc(graph, currentResistor,
                                                                     reconnectionResistor)
                parallelVoltage = systemCurrent * totalMiniParallelResistance
                for resistor in graph[currentResistor]:
                    resistanceSum = 0
                    resistorPassOne = resistor
                    resistorPassTwo = resistor
                    while resistorPassOne != reconnectionResistor:
                        resistanceSum += resistorPassOne.getResistance()
                        nextResistor = graph[resistorPassOne][0]
                        resistorPassOne = nextResistor
                    pathCurrent = parallelVoltage / resistanceSum
                    while resistorPassTwo != reconnectionResistor:
                        resistorPassTwo.setCurrent(pathCurrent)
                        nextResistor = graph[resistorPassTwo][0]
                        resistorPassTwo = nextResistor
                currentResistor = reconnectionResistor
                reconnectionResistor.setCurrent(systemCurrent)