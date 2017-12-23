""" calculator script which can perform addition, substraction, division and multiplication """

import click

@click.group()
def cli():
    """ click group """
    pass

@click.command()
@click.argument('input_1')
@click.argument('input_2')
def add(input_1, input_2):
    """ implimentation of addition """
    result = int(input_1) + int(input_2)
    click.echo(result)

@click.command()
@click.argument('input_1')
@click.argument('input_2')
def subtract(input_1, input_2):
    """ implimentation of substraction """
    result = int(input_1) - int(input_2)
    click.echo(result)

@click.command()
@click.argument('input_1')
@click.argument('input_2')
def multiply(input_1, input_2):
    """ implimentation of division """
    result = int(input_1) * int(input_2)
    click.echo(result)

@click.command()
@click.argument('input_1')
@click.argument('input_2')
def divide(input_1, input_2):
    """ implimentation of multiplication """
    result = int(input_1) / int(input_2)
    click.echo(result)

cli.add_command(add)
cli.add_command(subtract)
cli.add_command(multiply)
cli.add_command(divide)

if __name__ == '__main__':
    cli()