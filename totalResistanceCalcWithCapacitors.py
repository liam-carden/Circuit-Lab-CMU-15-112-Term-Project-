from getFinalComponent import *
from allInSeries import *
from Capacitor import *
from findReconnection import *
from subDataCreater import *

# calculates the total resistance of the circuit with the assumption that
# there are capacitors.
def totalResistanceCalcWithCapacitors(startingNode, graph, time):
    summy = 0
    endComponent = getFinalComponent(graph)
    component = startingNode.getComponent()
    
    if allInSeries(graph):
        while component != endComponent:
            if not isinstance(component, Capacitor):
                summy += component.getResistance()
            nextComponent = graph[component][0]
            component = nextComponent
        if not isinstance(endComponent, Capacitor):
            summy += endComponent.getResistance()
        return summy

    while component != endComponent:
        if len(graph[component]) == 1:
            if not isinstance(component, Capacitor):
                summy += component.getResistance()
            nextComponent = graph[component][0]
            component = nextComponent
        else:
            summy += component.getResistance()
            reconnectionComponent=findReconnection(graph, component, endComponent)
            subGraph = subDataCreater(graph, component, reconnectionComponent)
            subSummy = 0
            subSubSummy = 0
            subSystemContainsCapacitors = False
            onlyCapacitorChains = []
            onlyNonCapacitorChains = []
            for chain in subGraph:
                chainContainsCapacitors = False
                for componentX in chain:
                    if (chainContainsCapacitors == False) and isinstance(componentX, Capacitor):
                        subSystemContainsCapacitors = True
                        onlyCapacitorChains.append(chain)
                        chainContainsCapacitors = True
                if chainContainsCapacitors == False:
                    onlyNonCapacitorChains.append(chain)
            if subSystemContainsCapacitors:
                if time == 0:
                    for chain in onlyCapacitorChains:
                        for componentY in chain:
                            if not isinstance(componentY, Capacitor):
                                subSubSummy += componentY.getResistance()
                        if subSubSummy != 0:
                            subSummy += (subSubSummy)**(-1)
                        subSubSummy = 0
                else:
                    for chain in onlyNonCapacitorChains:
                        for componentZ in chain:
                            subSubSummy += componentZ.getResistance()
                        if subSubSummy != 0:
                            subSummy += (subSubSummy)**(-1)
                        subSubSummy = 0
            else:
                for subComponent in graph[component]:
                    while subComponent != reconnectionComponent:
                        if len(graph[subComponent]) == 1:
                            subSubSummy += subComponent.getResistance()
                            nextComponent = graph[subComponent][0]
                            subComponent = nextComponent
                        else:
                            pass
                    if subSubSummy != 0:
                        subSummy += (subSubSummy)**(-1)
                    subSubSummy = 0
            if subSummy != 0:
                summy += (subSummy)**(-1)
            subSummy = 0
            component = reconnectionComponent
    if not isinstance(endComponent, Capacitor):
        summy += endComponent.getResistance()
    return summy
