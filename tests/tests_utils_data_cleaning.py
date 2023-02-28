"""
Runs shot tests and multiple edge cases
for the functions imported from utils.py

tests_utils does not export any classes, exceptions, or functions
"""


import unittest
import os
import json

from rotten_tomatoes import CriticsDataCleaner, MoviesDataCleaner, OscarsDataCleaner, RegressionAnalysis, CorrelationAnalysis, plot_linear_fit

class TestUtilsDataCleaning(unittest.TestCase):

    """
    A class used to test the rotten_tomatoes.utils module

    ...

    Methods
    -------
    test_oscars_data(self)
        Description...

    """

    # One shot tests
    def test_smoke_cleaners(self):
        """ One shot test passes if..."""

        critics_data = CriticsDataCleaner().run()
        movies_data = MoviesDataCleaner().run()
        oscars_data = OscarsDataCleaner().run()

        self.assertTrue(True)

    def test_single_score(self):
        """ UPDATE ME"""

        cleaner = CriticsDataCleaner()
        
        score_to_test = {
            "A":90,
            "B":80,
            "4/5":90
        }

        for input, output in score_to_test.items():
            unittest.assertEquals(cleaner._clean_single_score(input), output)

    
    #How do I create a test to verify the CriticsDataCleaner._clean_single_score function works properly?

    # ideally, I'd like to manually create a dataframe with only a few rows and feed that dataframe to the CriticsDataCleaner._clean_single_score method

    # or, I could check specific lines in the full_data.csv?





    



if __name__ == '__main__':
    unittest.main()