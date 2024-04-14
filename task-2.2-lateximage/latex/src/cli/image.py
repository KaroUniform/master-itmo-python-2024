import click
import json

from src.latex.latex import generate_latex_table, generate_latex_image
from src.latex.file_io import save_to_tex_file

@click.command()
@click.argument('json_path', type=click.Path(exists=True))
@click.argument('img_path', type=click.Path(exists=True))
@click.option('-o', 'output_path', type=click.Path(), default='output.tex', help='Output file name for the LaTeX document (default value - ./output.tex).')
def image(json_path, img_path, output_path):
    """
    CLI command to generate a .tex file from a table defined in a JSON file with image.
    """
    # Read and parse table data from JSON file
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Generate LaTeX code for table
    latex_code = generate_latex_table(data)

    # Generate LaTeX code for image
    latex_code += generate_latex_image(img_path)

    # Save generated LaTeX code to file
    save_to_tex_file(latex_code, output_path)
    
    click.echo(f"LaTeX file '{output_path}' generated successfully from '{json_path} with '{img_path}'.")
