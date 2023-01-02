from PowerBar import *
from GroundBar import *

# class for Node Object
class Node(object):
    # constructor for node object
    def __init__(self, location):
        self.location = location
        self.component = None
        self.bar = None
        self.cords = (0,0)

    # returns that two nodes are equal if they are at the same location
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        if self.location == other.location:
            return True
        else:
            return False

    # returns True if the node has a component connected to it, False otherwise
    def hasComponent(self):
        return self.component != None

    # assigns a component to this node
    def assignComponent(self, component):
        self.component = component

    # returns the location of the node in data structure form
    # returns the row, side, and column
    def getLocation(self):
        return self.location

    # returns the voltage at this node
    def getVoltage(self):
        return self.bar.getVoltage()

    # assigns a bar object to this node
    def assignBar(self, bar):
        self.bar = bar

    # returns the bar assigned to this node
    def getBar(self):
        return self.bar

    # sets the coordinates of this node
    def setCords(self, cords):
        self.cords = cords

    # returns the (x,y) coordinates of this node
    def getCords(self):
        return self.cords

    # sets the Voltage of the node
    def setVoltage(self, newVoltage):
        if self.isGroundNode():
            return "Can not change ground node voltage"
        else:
            self.bar.setVoltage(newVoltage)

    # returns True if the node is connected to a power bar
    def isPowerNode(self):
        return isinstance(self.bar, PowerBar)

    # returns True if the node is connected to a ground bar
    def isGroundNode(self):
        return isinstance(self.bar, GroundBar)

    # returns the component that the node is connected to
    def getComponent(self):
        return self.component