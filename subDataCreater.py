# Creates a subdata structure of the graph from the startComponent to the
# endComponent given. 
# graph format will look like this example:
# {1:[2],2:[3,4],3:[5],4:[6],5:[6]}
def subDataCreater(graph, startComponent, endComponent):
    subGraph = []
    for currentComponent in graph[startComponent]:
        toGraph = []
        while currentComponent != endComponent:
            toGraph.append(currentComponent)
            nextComponent = graph[currentComponent][0]
            currentComponent = nextComponent
        subGraph.append(toGraph)

    return subGraph