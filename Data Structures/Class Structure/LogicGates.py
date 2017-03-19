class LogicGate(object):
    '''
    A definition for a series of gates
    '''

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    '''
    A definition for two input gates (AND, OR)
    '''

    def __init__(self, n, pinA=None, pinB=None):
        LogicGate.__init__(self, n)

        self.pinA = pinA
        self.pinB = pinB

    def getPinA(self):
        return int(input('Enter Pin A input for Gate: ' +
                         self.getLabel() + '--> '))

    def getPinB(self):
        return int(input('Enter Pin B input for Gate: ' +
                         self.getLabel() + '--> '))


class UrinaryGate(LogicGate):
    '''
    A definition for a single input gate
    '''
    def __init__(self, n, pin=None):
        LogicGate.__init__(self, n)

        self.pin = pin

    def getPin(self):
        return int(input('Enter Pin input for Gate: ' +
                         self.getLabel() + '-->'))


class AndGate(BinaryGate):
    '''
    A definition for a gate that adds two input values
    '''

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


def test_AndGate():

    g1 = AndGate("G1")
    g1.getOutput()

