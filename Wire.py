from Component import *

# *Class for Wire Objects
# sub-class of Component
class Wire(Component):
    # Constructor for Wires
    # Calls default Component constructor
    def __init__(self, startNode, endNode, color = "yellow"):
        super().__init__(startNode, endNode)
        self.color = color
        self.setNodeVoltages()
        self.current = 0
        
    # returns the color of the wire
    def getColor(self):
        return self.color

    # returns the current through the wire
    def getCurrent(self):
        return self.current
    
    # sets the current through the wire
    def setCurrent(self, current):
        self.current = current

    # sets the node voltages that the wire is connected to as well as their
    # bars
    def setNodeVoltages(self):
        if self.startNode.isPowerNode() and self.endNode.isGroundNode():
            pass
        elif self.startNode.isGroundNode() and self.endNode.isPowerNode():
            pass
        elif self.startNode.isGroundNode():
            self.endNode.setVoltage(0)
        elif self.endNode.isGroundNode():
            self.startNode.setVoltage(0)
        elif self.startNode.isPowerNode():
            self.endNode.setVoltage(self.startNode.getVoltage())
        elif self.endNode.isPowerNode():
            self.startNode.setVoltage(self.endNode.getVoltage())
        else:
            self.endNode.setVoltage(self.startNode.getVoltage)

    # Provides the string print out for Wires
    def __repr__(self):
        return f"Wire(color={self.color})"

    # returns the resistance of a wire (very small)
    def getResistance(self):
        return (1**(-14))
        # return 0 # alternate form where wires have 0 resistance