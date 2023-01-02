# orders components such that the startingNode of each component is actually
# where current will flow into while the endingNode is where current will
# flow out from
def orderComponents(vInNode):
    startingComponent = vInNode.getComponent()
    if vInNode != startingComponent.getStartNode():
        startingComponent.swapNodes()
    startingComponent.check()
    queue = [startingComponent.getEndNode()]
    while len(queue) > 0:
        currentNode = queue[0]
        if currentNode.isGroundNode():
            break
        currentBar = currentNode.getBar()
        barNodes = currentBar.getNodes()
        analyse = []
        for node in barNodes:
            if node.getComponent() != None and node != currentNode:
                analyse.append(node)
        for node in analyse:
            analyseComponent = node.getComponent()
            if not analyseComponent.isChecked():
                if node != analyseComponent.getStartNode():
                    analyseComponent.swapNodes()
                analyseComponent.check()
                childNode = analyseComponent.getEndNode()
                queue.append(childNode)
        queue.pop(0)