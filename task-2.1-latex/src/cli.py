import json

import click
from latex import generate_latex_table, generate_latex_image
from file_io import save_to_tex_file

@click.command()
@click.option('--input-json', default='../artifacts/input.json', type=click.Path(exists=True), help='Input JSON file with table data.')
@click.option('--output', default='../artifacts/1.tex', help='Output file name for the LaTeX document.')
def generate_table(input_json, output):
    """
    CLI command to generate a .tex file from a table defined in a JSON file.
    """
    with open(input_json, 'r') as file:
        data = json.load(file)

    latex_code = generate_latex_table(data)
    save_to_tex_file(latex_code, output)
    
    click.echo(f"LaTeX file '{output}' generated successfully from '{input_json}'.")


@click.command()
@click.option('--input-json', default='../artifacts/input.json', type=click.Path(exists=True), help='Input JSON file with table data.')
@click.option('--input-image', default='image.png', help='Input PNG image file.')
@click.option('--output', default='../artifacts/2.1.tex', help='Output file name for the LaTeX document.')
def generate_image_table(input_json, input_image, output):
    """
    CLI command to generate a .tex file from a table defined in a JSON file with image.
    """
    with open(input_json, 'r') as file:
        data = json.load(file)

    latex_code = generate_latex_table(data)
    latex_code += generate_latex_image(input_image)
    save_to_tex_file(latex_code, output)
    
    click.echo(f"LaTeX file '{output}' generated successfully from '{input_json} with '{input_image}'.")

@click.group()
def cli():
    """CLI Tool for various operations."""
    pass

cli.add_command(generate_table)
cli.add_command(generate_image_table)

if __name__ == "__main__":
    cli()