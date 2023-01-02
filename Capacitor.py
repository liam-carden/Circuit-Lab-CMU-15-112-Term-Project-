from Component import *

# *Class for Capacitor Objects
# sub-class of Component
class Capacitor(Component):
    # Constructor for Capacitors
    # Calls default Component constructor
    def __init__(self,startNode, endNode, name, capacitance):
        super().__init__(startNode,endNode)
        self.capacitance = capacitance
        self.name = name
    
    # Provides the string print out for Capacitors
    def __repr__(self):
        return f"Capacitor(name={self.name})"

    # returns the Capacitors Capacitance 
    def getCapacitance(self):
        return self.capacitance

    # Returns the name of the Capacitor
    def getName(self):
        return self.name

    # Returns 0 as the resistance for any Capacitor
    def getResistance(self):
        return 0