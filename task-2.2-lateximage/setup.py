from setuptools import setup, find_packages

setup(
    name='karo-latex',
    version='0.1.4',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        latex=latex.cli:cli
    ''',
)