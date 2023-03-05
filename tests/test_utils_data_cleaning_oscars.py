"""
Runs a smoke test, multiple one shot tests and multiple edge tests
for the functions imported from utils.data_cleaning module

test_utils_data_cleaning does not export any classes, exceptions, or functions
"""


import unittest
import pandas as pd

from rotten_tomatoes.utils.data_cleaning import ( # pylint: disable=E0401
    DataCleaner,
    OscarsDataCleaner,
    ValidationException
)


class TestUtilsDataCleaningOscars(unittest.TestCase):
    """ A class used to test the rotten_tomatoes.utils.data_cleaning module """

    # Smoke test
    def test_smoke_cleaner(self):
        """Smoke test passes if the class initializes."""
        self.assertIsInstance(OscarsDataCleaner(), DataCleaner)

    # One shot tests (base tests)
    def test_clean_oscars(self):
        """Test passes if the _clean function removes rows with None in the review_score column """
        cleaner = OscarsDataCleaner()

        dfs_to_test = [

            ({'year_film': [1, 2, 3],
             'category': [4, 5, 6],
             'film': [70.0, 80.0, 90.5],
             'winner':[10.0, None, "12"],
            }, 2),

            ({'film':[None, 11, 12],
             'winner': [None, None, "10/10"]
            }, 1),

            ({'film':[70, 11, 12],
             'winner': [75.0, 9.0, "10/10"]
            }, 3),

        ]

        for data, numrows in dfs_to_test:
            input_df =pd.DataFrame(data)
            self.assertEqual(cleaner._clean(input_df).shape[0], numrows)
    
    #@unittest.skip("need to update")
    def test_validate_movies(self):
        """Passes if no error thrown by _validate"""

        cleaner = OscarsDataCleaner()

        flag = False

        df_to_test = {'year_film': [1995, 2018, 2008],
             'category': ["Best Picture", "Best Actress", "Best Motion Picture"],
             'film':["ABC123", "Some Movie", 6],
             'winner': [1.0, 3.0, 1.0]
            }

        input_df =pd.DataFrame(df_to_test)
        cleaner._validate(input_df)

        flag = True
        self.assertTrue(flag)

    # Edge tests
    #@unittest.skip("need to update")
    def test_validate_edge(self):
        """Passes if Validation  Exeption thrown by _validate_rating_col """

        cleaner = OscarsDataCleaner()

        cleaner.keep_columns = ["year_film", "category", "film", "winner"]

        dfs_to_test = [
            {'film':["ABC123", "Some Movie", 6],
             'winner': [1.0, 3.0, 1.0]
            },

            {'year_film': [1995, 2018, 2008],
             'category': ["Best Picture", "Best Actress", "Best Motion Picture"]
            }
        ]

        for data in dfs_to_test:
            input_df =pd.DataFrame(data)
            print(data)
            self.assertRaises(ValidationException, cleaner._validate, input_df)


if __name__ == "__main__":
    unittest.main()
