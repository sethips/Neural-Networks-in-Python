import math
class Neuron(object):
    """docstring for Neuron."""
    def __init__(self, val):
        self.val = val
        self.activate()
        self.derive()
    def activate(self):
        self.activatedVal = self.val/(1 + math.fabs(self.val))
    def derive(self):
        self.derivedVal = self.activatedVal * ( 1 - self.activatedVal )
    def setVal(val):
        self.val = val
        activate()
        derive()
    def getVal(self):
        return self.val
    def getActivatedVal(self):
        return self.activatedVal
    def getDerivedVal(self):
        return self.derivedVal
