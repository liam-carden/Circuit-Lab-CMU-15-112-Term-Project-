# class for a ground bar object
class GroundBar(object):
    # constructor for ground bar object
    def __init__(self, side):
        self.side = side

    # returns True always as a ground bar is always grounded
    def isGrounded(self):
        return True

    # ground always has a voltage of 0
    def getVoltage(self):
        return 0