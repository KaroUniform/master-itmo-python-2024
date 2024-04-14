# Usage

## Create .tex file

Download karo-latex package from testPyPI:

```bash
pip install -i https://test.pypi.org/simple/ karo-latex
```

And use installed package: 

```bash
latex --help
```

## Create pdf file from tex file

You need to buid image:

```bash
docker build -t pdflatex .
```

Then use built image like this:
```python
docker run -it --rm -v "${PWD}:/root/shared/folder" --name pdflatex pdflatex <filename>.tex
```
