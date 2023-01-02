# Power bar class which acts as the voltage source for the breadboard
class PowerBar(object):

    # contructor for the power bar, sets the default voltage level to 9V
    def __init__(self, side):
        self.side = side
        self.voltage = 9

    # sets the voltage to a new given voltage
    def setVoltage(self, voltage):
        self.voltage = voltage

    # returns the power bars voltage
    def getVoltage(self):
        return self.voltage