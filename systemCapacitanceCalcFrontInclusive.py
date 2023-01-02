from Capacitor import *

# Calculates the capacitance of a graph from the starting component to the end
# component that includes the capacitance of the starting component.
def systemCapacitanceCalcFrontInclusive(start, graph, end):
    component = start
    summy = 0
    while component != end:
        
        if len(graph[component]) == 1:
            if isinstance(component, Capacitor):
                summy += (component.getCapacitance())**(-1)
            nextComponent = graph[component][0]
            component = nextComponent

        else:
            pass

    returnSummy = 0

    if summy != 0:
        returnSummy = (summy)**(-1)
    
    return returnSummy