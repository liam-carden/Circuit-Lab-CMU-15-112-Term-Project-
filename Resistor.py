from Component import *

# *Class for Resistor Objects
# sub-class of Component
class Resistor(Component):
    # Constructor for Resistors
    # Calls default Component constructor
    def __init__(self, startNode, endNode, name, resistance):
        super().__init__(startNode, endNode)
        self.resistance = resistance
        self.name = name
    
    # Provides the string print out for Resistors
    def __repr__(self):
        return f"Resistor(name={self.name})"
        
    # returns the Resistance of the resistor
    def getResistance(self):
        return self.resistance

    # returns the name of the resistor
    def getName(self):
        return self.name