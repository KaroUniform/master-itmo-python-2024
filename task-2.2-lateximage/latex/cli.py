import click 

from src.cli.image import image
from src.cli.table import table

@click.group()
def cli():
    pass

cli.add_command(table)
cli.add_command(image)

if __name__ == "__main__":
    cli()