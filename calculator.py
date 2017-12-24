""" calculator script which can perform addition, substraction, division and multiplication """

import click

@click.command()
@click.option('--add', nargs = 2, type = float)
@click.option('--subtract', nargs = 2, type = float)
@click.option('--multiply', nargs = 2, type = float)
@click.option('--divide', nargs = 2, type = float)
def cli(add,subtract,multiply,divide):
    """ controll system """
    if add:
        """ implimentation of addition """
        click.echo(add[0] + add[1])
    elif subtract:
        """ implimentation of substraction """
        click.echo(subtract[0] - subtract[1])
    elif multiply:
        """ implimentation of multiplication """
        click.echo(multiply[0] * multiply[1])
    elif divide:
        """ implimentation of division """
        click.echo(divide[0] / divide[1])

if __name__ == '__main__':
    cli()