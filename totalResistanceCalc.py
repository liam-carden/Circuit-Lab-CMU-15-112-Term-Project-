from containsNoCapacitors import *
from totalResistanceCalcNoCapacitors import *
from totalResistanceCalcWithCapacitors import *

# calculates the total resistance of the circuit
def totalResistanceCalc(startingNode, graph, components, time):
    if containsNoCapacitors(components):
        return totalResistanceCalcNoCapacitors(startingNode, graph)
    else:
        return totalResistanceCalcWithCapacitors(startingNode, graph, time)