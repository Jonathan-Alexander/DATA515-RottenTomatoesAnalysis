from distutils.core import setup
from setuptools import find_packages

setup(name="rottentomatoes",
    version='1.0',
    description='Rotten Tomatoes Analysis Package',
    author='RottenTomatoesGroup',
    author_email='jonalex@uw.edu',
    url='https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis',
    test_suite='tests',
    packages=find_packages(),
)