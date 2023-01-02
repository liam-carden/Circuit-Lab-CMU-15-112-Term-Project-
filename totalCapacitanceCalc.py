from getFinalComponent import *
from allInSeries import *
from Capacitor import *
from findReconnection import *

# calculates the total capacitance of the circuit
def totalCapacitanceCalc(startingNode, graph):
    summy = 0
    endComponent = getFinalComponent(graph)
    component = startingNode.getComponent()

    if allInSeries(graph):
        while component != endComponent:
            if isinstance(component, Capacitor):
                summy += (component.getCapacitance())**(-1)
            nextComponent = graph[component][0]
            component = nextComponent
        if isinstance(endComponent, Capacitor):
            summy += (endComponent.getCapacitance())**(-1)
        return (summy)**(-1)
    
    while component != endComponent:
        if len(graph[component]) == 1:
            if isinstance(component, Capacitor):
                summy += (component.getCapacitance())**(-1)
            nextComponent = graph[component][0]
            component = nextComponent
        else:
            if isinstance(component, Capacitor):
                summy += (component.getCapacitance())**(-1)
            reconnectionComponent = findReconnection(graph, component, endComponent)
            subSummy = 0
            subSubSummy = 0
            for subComponent in graph[component]:
                while subComponent != reconnectionComponent:
                    if len(graph[subComponent]) == 1:
                        if isinstance(subComponent, Capacitor):
                            subSubSummy += (subComponent.getCapacitance())**(-1)
                        nextComponent = graph[subComponent][0]
                        subComponent = nextComponent
                    else:
                        pass
                if subSubSummy != 0:
                    subSubSummy = (subSubSummy)**(-1)
                subSummy += subSubSummy
                subSubSummy = 0
            if subSummy != 0:
                summy += (subSummy)**(-1)
            component = reconnectionComponent
    if isinstance(endComponent, Capacitor):
        summy += (endComponent.getCapacitance())**(-1)
    return (summy)**(-1)