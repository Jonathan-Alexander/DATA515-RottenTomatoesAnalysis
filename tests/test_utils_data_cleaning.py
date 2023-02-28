"""
Runs shot tests and multiple edge cases
for the functions imported from utils.py

tests_utils does not export any classes, exceptions, or functions
"""


import unittest
import os
import json

from rotten_tomatoes.utils.data_cleaning import (
    DataCleaner, 
    CriticsDataCleaner,
    MoviesDataCleaner,
    BestPictureOscarsDataCleaner,
    AnyWinOscarsDataCleaner,
)


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
        """One shot test passes if the class initializes."""
        self.assertIsInstance(CriticsDataCleaner(), DataCleaner)
        self.assertIsInstance(MoviesDataCleaner(), DataCleaner)
        self.assertIsInstance(AnyWinOscarsDataCleaner(), DataCleaner)
        self.assertIsInstance(BestPictureOscarsDataCleaner(), DataCleaner)


    def test_single_score(self):
        """UPDATE ME"""

        cleaner = CriticsDataCleaner()

        score_to_test = {"A": 95, "B": 85, "4/5": 80.0}

        for input, output in score_to_test.items():
            self.assertEquals(cleaner._clean_single_score(input), output)

    # How do I create a test to verify the CriticsDataCleaner._clean_single_score function works properly?

    # ideally, I'd like to manually create a dataframe with only a few rows and feed that dataframe to the CriticsDataCleaner._clean_single_score method

    # or, I could check specific lines in the full_data.csv?


if __name__ == "__main__":
    unittest.main()
