from distutils.core import setup

setup(name="rottentomatoes",
    version='1.0',
    description='Rotten Tomatoes Analysis Package',
    author='RottenTomatoesGroup',
    author_email='jonalex@uw.edu',
    packages=['rotten_tomatoes', 'tests'],
    url='https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis',
    test_suite='tests',
    install_requires=[
        '<matplotlib>',
        '<numpy>',
        '<pandas>',
        '<seaborn>',
        '<scikit-learn>',
        '<distutils>',
        '<pytest>'
    ]


)