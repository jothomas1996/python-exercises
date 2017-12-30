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
        return self.output


""" basic gates classes """

class AndGate(Gate):
    """ class for AND gate """

    def logic(self):
        self.output = self.input[0][0] and self.input[0][1]

class OrGate(Gate):
    """ class for OR gate """

    def logic(self):
        self.output = self.input[0][0] or self.input[0][1]

class NotGate(Gate):
    """ class for NOT gate """

    def logic(self):
        self.output = not self.input[0]


""" Universal gates """

class NandGate(AndGate, NotGate):
    """ class for nand gate """
    def logic(self):
        andGate = AndGate(self.input[0])
        andGate.logic()
        notGate = NotGate(andGate.output)
        notGate.logic()
        self.output = notGate.output

class NorGate(OrGate, NotGate):
    """ class for nor gate """
    def logic(self):
        orGate = OrGate(self.input[0])
        orGate.logic()
        notGate = NotGate(orGate.output)
        notGate.logic()
        self.output = notGate.output


""" excetion code """
@click.command()
@click.option('--nand', nargs = 2, type = int)
@click.option('--nor', nargs = 2, type = int)
def cli(nand,nor):
    if nand:
        gate = NandGate(nand)
        gate.logic()
        click.echo(gate.output)
    elif nor:
        gate = NorGate(nor)
        gate.logic()
        click.echo(gate.output)

if __name__ == '__main__':
    cli()

""" extraction system """