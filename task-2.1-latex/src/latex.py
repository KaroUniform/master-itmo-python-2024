from typing import Any, List


def generate_latex_table(data: List[List[Any]]) -> str:
    """
    Generates a LaTeX table code from the provided data.

    Parameters:
    - data (List[List[Any]]): A 2D list containing rows of the table.

    Returns:
    - str: A string containing the formatted LaTeX table code.
    """
    latex_code = "\\begin{tabular}{|" + "l|"*len(data[0]) + "}\n\\hline\n"
    for row in data:
        latex_code += " & ".join(map(str, row)) + " \\\\\n\\hline\n"
    latex_code += "\\end{tabular}"
    return latex_code

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
    latex_code = f"""
\\begin{{figure}}[ht]
\\centering
\\includegraphics[width=0.8\\textwidth]{{{filepath}}}
\\caption{{{caption}}}
\\label{{{label}}}
\\end{{figure}}
"""
    return latex_code