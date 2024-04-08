import click


@click.command()
@click.argument('file', type=click.File('r'), default='-')
def number_lines(file):
    """
    Пронумеровать строки из файла или stdin.
    """
    for line_number, line in enumerate(file, start=1):
        click.echo(f"{line_number}\t{line}", nl=False)

if __name__ == '__main__':
    number_lines()