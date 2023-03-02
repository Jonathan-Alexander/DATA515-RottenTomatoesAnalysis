"""
Runs a smoke test, multiple one shot tests and multiple edge tests
for the functions imported from utils.data_cleaning.DataCleaning

test_utils_data_cleaning_datacleaning does not export any classes, exceptions, or functions
"""


import unittest
import pandas as pd

from rotten_tomatoes.utils.data_cleaning import ( # pylint: disable=E0401
    DataCleaner
)

class TestUtilsDataCleaning(unittest.TestCase):
    """ A class used to test the DataCleaning class in the
    rotten_tomatoes.utils.data_cleaning module """

    # Smoke test
    def test_smoke_cleaner(self):
        """Smoke test passes if the class initializes."""
        self.assertIsInstance(DataCleaner(), DataCleaner)
        cleaner = DataCleaner()
    
    # One shot test
    # def test_data_cleaner(self):
    #     try:
    #         cleaner = DataCleaner()
    #     except Exception:
    #         self.fail("myFunc() raised ExceptionType unexpectedly!")
    #     #self.assertTrue(True)
    
    # One shot test
    def test_read_clean(self):
        cleaner = DataCleaner()
        
        df_to_test = {'year_film': [1995, 2018, 2008],
             'category': ["Best Picture", "Best Actress", "Best Motion Picture"],
             'film':["ABC123", "Some Movie", 6],
             'winner': [1.0, 3.0, 1.0]
            }

        data = pd.DataFrame(df_to_test)
        self.assertRaises(NotImplementedError, cleaner._clean, data)
        self.assertRaises(NotImplementedError, cleaner._read)

        with self.assertRaises(NotImplementedError):
            cleaner.run()


if __name__ == "__main__":
    unittest.main()