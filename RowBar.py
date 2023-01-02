# class for RowBar object
class RowBar(object):
    # Constructor for RowBar object
    def __init__(self, row, side):
        self.row = row
        self.side = side
        self.voltage = None
        self.nodes = []

    # sets the voltage of this RowBar to the specified voltage level
    def setVoltage(self, voltage):
        self.voltage = voltage

    # returns the specified votlage level
    def getVoltage(self):
        return self.voltage

    # adds the given node to the RowBar's list of nodes
    def addNode(self, node):
        self.nodes.append(node)

    # retuns the RowBars list of nodes
    def getNodes(self):
        return self.nodes

    