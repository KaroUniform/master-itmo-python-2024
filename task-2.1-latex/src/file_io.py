# Function to save the LaTeX code to a file
def save_to_tex_file(latex_code: str, filename:str="output.tex"):
    """
    Saves the provided LaTeX code to a file.

    Parameters:
    - latex_code: A string containing LaTeX code.
    - filename: The name of the file to save the code.
    """
    # Preparing the complete LaTeX document code
    full_document = "\\documentclass{article}\n\\begin{document}\n" + latex_code + "\n\\end{document}"
    # Writing to the file
    with open(filename, "w") as file:
        file.write(full_document)