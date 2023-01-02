# finds the reconnection point of a parallel system from one component. The
# given endComponent is the end of the entire circuit
def findReconnection(graph, component, endComponent):
    storageSet = set()
    storageList = []
    superStorageList = []
    toSuper = []
    for subComponent in graph[component]:
        for comp in graph[subComponent]:
            storageSet.add(comp)
            storageList.append(comp)
    # case that deals with simple parallel
    if len(storageSet) == 1:
        return storageList[0]
    else:
        for subComponent in graph[component]:
            while subComponent != endComponent:
                toSuper.append(subComponent)
                nextComponent = graph[subComponent][0]
                subComponent = nextComponent
            toSuper.append(endComponent)
            superStorageList.append(toSuper)
            toSuper = []
        firstChain = superStorageList[0]
        for chain in superStorageList:
            closest = endComponent
            if chain == firstChain:
                continue
            else:
                for index in range(len(chain)):
                    for indexFirst in range(len(firstChain)):
                        if firstChain[indexFirst] == chain[index]:
                            closest = chain[index]
                            return closest
        return closest