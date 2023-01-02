from getFinalComponent import *
from allInSeries import *
from findReconnection import *

# calculates the total Resistance of the circuit with the assumption that
# there are no capacitors.
def totalResistanceCalcNoCapacitors(startingNode, graph):
    summy = 0
    endResistor = getFinalComponent(graph)
    resistor = startingNode.getComponent()
    
    if allInSeries(graph):
        while resistor != endResistor:
            summy += resistor.getResistance()
            nextResistor = graph[resistor][0]
            resistor = nextResistor
        summy += endResistor.getResistance()
        return summy

    while resistor != endResistor:
        if len(graph[resistor]) == 1:
            summy += resistor.getResistance()
            nextResistor = graph[resistor][0]
            resistor = nextResistor
        else:
            summy += resistor.getResistance()
            reconnectionResistor = findReconnection(graph, resistor, endResistor)
            subSummy = 0
            subSubSummy = 0
            for subResistor in graph[resistor]:
                while subResistor != reconnectionResistor:
                    if len(graph[subResistor]) == 1:
                        subSubSummy += subResistor.getResistance()
                        nextResistor = graph[subResistor][0]
                        subResistor = nextResistor
                    else:
                        pass
                subSummy += (subSubSummy)**(-1)
                subSubSummy = 0
            summy += (subSummy)**(-1)
            subSummy = 0
            resistor = reconnectionResistor
    summy += endResistor.getResistance()
    return summy