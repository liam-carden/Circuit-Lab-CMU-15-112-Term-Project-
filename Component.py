
# *Parent Class For All Components
# contains default information used for all components
class Component(object):
    # constructor for a component
    def __init__(self, startNode, endNode):
        self.startNode = startNode
        self.endNode = endNode
        self.row1, self.side1, self.col1 = startNode.getLocation()
        self.row2, self.side2, self.col2 = endNode.getLocation()
        self.x1, self.y1 = startNode.getCords()
        self.x2, self.y2 = endNode.getCords()
        startNode.assignComponent(self)
        endNode.assignComponent(self)
        self.checked = False
        self.current = 0
        self.voltage = 0

    # swaps the Nodes of a component
    # *used to help arrange components to have the correct orientation
    def swapNodes(self):
        temp = self.startNode
        self.startNode = self.endNode
        self.endNode = temp

    # returns the voltage drop over a given component
    def getVoltage(self):
        return self.voltage

    # sets the voltage drop over a given component
    def setVoltage(self, voltage):
        self.voltage = voltage

    # returns whether or not the component has been checked
    #* used in ordering of components
    def isChecked(self):
        return self.checked

    # sets the component as having been checked
    #* used in ordering of components
    def check(self):
        self.checked = True

    # returns the starting node of a component
    def getStartNode(self):
        return self.startNode

    # returns the ending node of a component
    def getEndNode(self):
        return self.endNode

    # returns the cordinates of the components starting node as a tuple
    def getStartNodeCords(self):
        return (self.x1, self.y1)

    # returns the cordiantes of the components ending node as a tuple
    def getEndNodeCords(self):
        return (self.x2, self.y2)

    # returns whether or not the component is connected to ground
    def isGroundComponent(self):
        return self.startNode.isGroundNode() or self.endNode.isGroundNode()

    # returns whether or not the component is connected to power
    def isPowerComponent(self):
        return self.startNode.isPowerNode() or self.endNode.isPowerNode()

    # returns the power node of a component if one exists
    def getPowerNode(self):
        if not self.isPowerComponent():
            return None
        elif self.startNode.isPowerNode():
            return self.startNode
        else:
            return self.endNode

    # swaps the nodes of a component
    def flipNodes(self):
        temp = self.startNode
        self.startNode = self.endNode
        self.endNode = temp

    # returns the current running through the component
    def getCurrent(self):
        return self.current
    
    # sets the current running through the component
    def setCurrent(self, current):
        self.current = current