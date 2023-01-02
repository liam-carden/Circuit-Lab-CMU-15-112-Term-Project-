
#* creates the data structure of an adjacency list inside a dictionary
# graph format will look like this example:
# {1:[2],2:[3,4],3:[5],4:[6],5:[6]}
# Information on what kinds of data structures come from the website for
# 15-388: https://www.datasciencecourse.org
def createDataStructure(startingNode):
    startingComponent = startingNode.getComponent()
    graph = {}
    queue = [startingComponent.getEndNode()]
    while len(queue) > 0:
        currentNode = queue[0]
        if currentNode.isGroundNode():
            break
        currentBar = currentNode.getBar()
        barNodes = currentBar.getNodes()
        componentsToAssign = []
        for node in barNodes:
            if (node.getComponent() != None 
                and node == node.getComponent().getStartNode()):
                    componentsToAssign.append(node.getComponent())
                    queue.append(node.getComponent().getEndNode())
        graph[currentNode.getComponent()] = componentsToAssign
        queue.pop(0)

    return graph