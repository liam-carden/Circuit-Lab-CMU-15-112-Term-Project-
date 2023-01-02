from containsNoCapacitors import *
from resistorOnlyCurrentAnalysis import *
from timeZeroCurrentAnalysis import *
from timeFiveTaoCurrentAnalysis import *

# Analyses the current of the circuit
def currentAnalysis(powerNode, graph, components, time, systemCurrent):
    if containsNoCapacitors(components):
        resistorOnlyCurrentAnalysis(powerNode, graph, components, systemCurrent)
    else:
        if time == 0:
            timeZeroCurrentAnalysis(powerNode, graph, components, systemCurrent)
        else:
            timeFiveTaoCurrentAnalysis(powerNode, graph, components)