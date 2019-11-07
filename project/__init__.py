import click
from .commands.test import test

@click.group()
def cli():
    """Interface de linha de comando (CLI) para simular autômatos finitos e principais algoritmos existente sobre autômatos."""
    pass

cli.add_command(test)
