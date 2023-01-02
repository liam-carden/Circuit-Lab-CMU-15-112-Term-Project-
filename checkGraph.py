from Component import *

# Checks the graph to ensure that components still remain
# currently unused, but good to keep incase it needs to be.
def checkGraph(startingComponent, graph, endComponent):
    newGraph = {}

    # create new graph
    for keyComponent in graph:
        for subComponent in graph[keyComponent]:
            if (not isinstance(keyComponent, Component) 
                and not isinstance(subComponent, Component)):
                newValue = (newGraph.get(keyComponent,[]))
                newValue.append(subComponent)
                newGraph[keyComponent] = newValue

    # check start is there
    if startingComponent not in newGraph:
        return None

    # check end is there
    containsEnd = False
    for key in newGraph:
        for subComponent in newGraph[key]:
            if subComponent == endComponent:
                containsEnd = True
    if not containsEnd:
        return None

    moveMade = True
    while moveMade:
        moveMade = False
        # remove connections that arent keys
        for key in newGraph:
            for subComponent in newGraph[key]:
                if subComponent == endComponent:
                    continue
                if subComponent not in newGraph:
                    moveMade = True
                    newGraph[key].remove(subComponent)

        # remove keys that arent connections
        connections = set()
        for key in newGraph:
            for connection in newGraph[key]:
                connections.add(connection)
        keys = []
        for key in newGraph:
            keys.append(key)

        for key in keys:
            if key == startingComponent:
                continue
            if key not in connections:
                del newGraph[key]
                moveMade = True

        # remove empty keys
        keys = []
        for key in newGraph:
            keys.append(key)

        for key in keys:
            if newGraph[key] == []:
                del newGraph[key]
                moveMade = True


        # check start is there
        if startingComponent not in newGraph:
            return None

        # check end is there
        containsEnd = False
        for key in newGraph:
            for subComponent in newGraph[key]:
                if subComponent == endComponent:
                    containsEnd = True
        if not containsEnd:
            return None

    if newGraph == {}:
        return None
    else:
        return newGraph