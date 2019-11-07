import click

@click.command('test', short_help="Comando para testar a CLI.")
@click.argument('value', required=False, type=str)
def test(value=None):
    """Pequeno comando de teste para a CLI."""
    click.echo('Exibição de texto após comando \'test\'')
    if value != None:
        click.echo('Valor: {}'.format(value))
