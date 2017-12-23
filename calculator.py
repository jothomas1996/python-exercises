""" calculator script which can perform addition, substraction, division and multiplication """

import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--input_1', default = 0, help = 'First input value')
@click.option('--input_2', default = 0, help = 'Second input value')
def add(input_1, input_2):
    """ implimentation of addition """
    print input_1 + input_2,

@click.command()
@click.option('--input_1', default = 0, help = 'First input value')
@click.option('--input_2', default = 0, help = 'Second input value')
def subtract(input_1, input_2):
    """ implimentation of substraction """
    print input_1 - input_2,

@click.command()
@click.option('--input_1', default = 0, help = 'First input value')
@click.option('--input_2', default = 0, help = 'Second input value')
def division(input_1, input_2):
    """ implimentation of division """
    print input_1 / input_2,

@click.command()
@click.option('--input_1', default = 0, help = 'First input value')
@click.option('--input_2', default = 0, help = 'Second input value')
def multiply(input_1, input_2):
    """ implimentation of multiplication """
    print input_1 * input_2,