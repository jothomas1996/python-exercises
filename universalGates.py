""" creating  universal gates - NAND and NOR """

import click

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
        print 'logic'
        return self.output


""" basic gates classes """

class AndGate(Gate):
    """ class for AND gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]

class OrGate(Gate):
    """ class for OR gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]

class NotGate(Gate):
    """ class for NOT gate """

    def logic(self):
        self.output = not self.input[0]


""" Universal gates """

class NandGate(AndGate):
    """ class for nand gate """
    def logic(self):
        andGate = super(self, nand).logic()
        NotGate.__init__(self, andGate)
        NotGate.logic(self)

class NorGate(OrGate, NotGate):
    """ class for nor gate """
    def logic(self):
        orGate = super(self, nor).logic()
        NotGate.__init__(self, orGate)
        NotGate.logic(self)


""" excetion code """
@click.command()
@click.option('--nand', nargs = 2, type = bool)
@click.option('--nor', nargs = 2, type = bool)
def cli(nand,nor):
    if nand:
        gate = NandGate(nand)
        print gate.output
    elif nor:
        gate = NorGate(nand)
        click.echo(gate.output)

if __name__ == '__main__':
    cli()

""" extraction system """