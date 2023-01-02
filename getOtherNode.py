# given a component and a node, returns the other node of the same component
def getOtherNode(component, node):
    if node == component.startNode:
        return component.endNode
    else:
        return component.startNode