""" creating  universal gates - NAND and NOR """

class Gate(object):
    """ base gate class """

    def __init__(self, *args):
        """ initialise the class """
        self.input = args
        self.output = None

    def logic(self):
        """ gate function """
        raise NotImplementedError

    def output(self):
        """ output of the gate """
        self.logic()
        return self.output

""" basic gates classes """
class AndGate(Gate):
    """ class representing AND gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]


class OrGate(Gate):
    """ class representing OR gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]


class NotGate(Gate):
    """ class representing NOT gate """

    def logic(self):
        self.output = not self.input[0]

class NandGate(AndGate, NotGate):
    pass

class NorGate(OrGate, NotGate):
    pass
