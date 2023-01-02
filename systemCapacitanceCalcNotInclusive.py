from Capacitor import *

# Calculates the capacitance of a graph from the starting component to the end
# component that does not include the capacitance of the starting component.
def systemCapacitanceCalcNotInclusive(start, graph, end):
    summy = 0
    for subComponent in graph[start]:
        subSummy = 0
        toSum = 0
        component = subComponent
        while component != end:
            if len(graph[component]) == 1:
                if isinstance(component, Capacitor):
                    subSummy += (component.getCapacitance())**(-1)
                nextComponent = graph[component][0]
                component = nextComponent
            else:
                pass
        
        if subSummy != 0:
            toSum = (subSummy)**(-1)
        summy += toSum

    return summy
