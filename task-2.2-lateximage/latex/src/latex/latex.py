from typing import Any, List
from pathlib import PureWindowsPath, PurePosixPath

# Function for generating LaTeX table code  
def generate_latex_table(data: List[List[Any]]) -> str:
    """
    Generates a LaTeX table code from the provided data.

    Parameters:
    - data (List[List[Any]]): A 2D list containing rows of the table.

    Returns:
    - str: A string containing the formatted LaTeX table code.
    """
    # Start of the table and setting alignment for each column
    latex_code = "\\begin{tabular}{|" + "l|"*len(data[0]) + "}\n\\hline\n"
    # Adding rows of data
    for row in data:
        latex_code += " & ".join(map(str, row)) + " \\\\\n\\hline\n"
    # Ending the table
    latex_code += "\\end{tabular}"
    return latex_code

# Function for generating LaTeX image code  
def generate_latex_image(filepath: str, caption: str = "Image", label: str = "fig:image") -> str:
    """
    Generates LaTeX code to include an image.

    Parameters:
    - filepath (str): Path to the image file.
    - caption (str): Caption for the image.
    - label (str): Reference label for the image.

    Returns:
    - str: A string containing the LaTeX code to include the image.
    """
    path = PureWindowsPath(filepath)

    latex_code = f"""
\\begin{{figure}}[t]
\\includegraphics[width=1cm, height=1cm]{{{PurePosixPath(path)}}}
\\end{{figure}}
"""
    return latex_code