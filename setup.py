import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name = 'SePyrability',
    packages = ['sepyrability'],
    version = '0.0.1',
    license='MIT',
    description = 'Python implementation of the multiscale separability metric.', 
    long_description = README,
    author = 'João Renato Ribeiro manesco',
    author_email = 'joaorenatorm@gmail.com',     
    url = 'https://github.com/jrjoaorenato/SePYrability',   
    download_url = 'https://github.com/jrjoaorenato/SePYrability/archive/v0.0.1.tar.gz', 
    keywords = ['Separability', 'Metric'], 
    install_requires=[
            'numpy',
            'matplotlib',
        ],
    classifiers=[
    'Development Status :: 3 - Alpha',    
    'Intended Audience :: Developers',   
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3'
    ],
)
