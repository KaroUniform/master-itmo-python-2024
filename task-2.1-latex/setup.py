from setuptools import setup, find_packages

setup(
    name='pieska',  
    version='0.1.2',  
    author='Karo Uniform',  
    author_email='snow.leopard.111@yandex.ru',  
    description='A LaTeX document generator',  
    packages=find_packages(where="src"),  
    package_dir={"": "src"},  
    install_requires=[ 
        'Click',  
    ],
    entry_points={  
        'console_scripts': [
            'latex-generator=cli:main', 
        ],
    },
)
