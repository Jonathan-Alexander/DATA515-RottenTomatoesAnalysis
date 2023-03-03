"""
Runs a smoke test, multiple one shot tests and multiple edge tests
for the functions imported from utils.data_cleaning module

test_utils_data_cleaning does not export any classes, exceptions, or functions
"""


import unittest
import pandas as pd

from rotten_tomatoes.utils.data_cleaning import ( # pylint: disable=E0401
    DataCleaner,
    CriticsDataCleaner,
    MoviesDataCleaner,
    BestPictureOscarsDataCleaner,
    AnyWinOscarsDataCleaner,
)


class TestUtilsDataCleaning(unittest.TestCase):

    """ A class used to test the rotten_tomatoes.utils.data_cleaning module """

    # Smoke test
    def test_smoke_cleaners(self):
        """Smoke test passes if the class initializes."""
        self.assertIsInstance(CriticsDataCleaner(), DataCleaner)
        self.assertIsInstance(MoviesDataCleaner(), DataCleaner)
        self.assertIsInstance(AnyWinOscarsDataCleaner(), DataCleaner)
        self.assertIsInstance(BestPictureOscarsDataCleaner(), DataCleaner)


    # One shot tests
    def test_single_score_critics(self):
        """Input values from scores_to_test dict passed to cleaner._clean_single_score function.
        Test passes if _clean_single_score returns the corresponding output values
        from the scores_to_test dict """

        cleaner = CriticsDataCleaner()
        # input : expected output
        scores_to_test = {
            # manual_corrections
            "35/4": 87.5,  # Assuming 3.5/4
            "67/10": 67.0,
            "87/10": 87.0,
            "920": 92.0,
            "76/10": 76.0,
            "75/10": 75.0,
            "910": 91.0,
            "25/4": 62.5,  # Assuming 2.5/4
            "45/5": 90.0,
            "73/10": 73.0,
            # substitutions
            "A+": 98,
            "A": 95,
            "A-": 93,
            "B+": 88,
            "B": 85,
            "B-": 83,
            "C+": 78,
            "C": 75,
            "C-": 73,
            "D+": 68,
            "D": 65,
            "D-": 63,
            "E": 50,
            "F": 40,
            # fractions
            "3/5": 60,
            "7/10": 70,
            "2/0": None,
            "3/1": 100,
            # number scores
            "110": 100,
            "60":60,
            "-19":-19
            }

        for input_str, output in scores_to_test.items():
            self.assertEqual(cleaner._clean_single_score(input_str), output)

    def test_clean_critics(self):
        """Test passes if the _clean function moves rows with None in the review_score column """

        cleaner = CriticsDataCleaner()

        dfs_to_test = [

            ({'rotten_tomatoes_link': [1, 2, 3],
             'critic_name': [4, 5, 6],
             'top_critic': [7, 8, 9],
             'review_type':[10, 11, 12],
             'review_score': ["A+", None, "10/10"]
            }, 2),

            ({'review_type':[10, 11, 12],
             'review_score': [None, None, "10/10"]
            }, 1),

            ({'review_type':[10, 11, 12],
             'review_score': ["A", "C-", "10/10"]
            }, 3)

        ]

        for data, numrows in dfs_to_test:
            input_df =pd.DataFrame(data)
            self.assertEqual(cleaner._clean(input_df).shape[0], numrows)

    def test_validate_critics(self):
        """Passes if no error thrown by cleaner._validate"""

        cleaner = CriticsDataCleaner()

        flag = False

        df_to_test = {'rotten_tomatoes_link': [1, 2, 3],
             'critic_name': [4, 5, 6],
             'top_critic': [7, 8, 9],
             'review_type':[10, 11, 12],
             'review_score': ["A+", None, "10/10"]
            }

        input_df =pd.DataFrame(df_to_test)
        cleaner._validate(input_df)

        flag = True
        self.assertTrue(flag)

    # Edge tests
    def test_single_score_edge_critics(self):
        """Test passes if value error is thrown if every value in scores_to_test_for_error
        is passed to the clenaer._clean_single_score function"""

        cleaner = CriticsDataCleaner()

        scores_to_test_for_error = [
            "G",
            "some multi-word string",
            "**",
            "?/10",
            "3?/89"
        ]

        for input_str in scores_to_test_for_error:
            self.assertRaises(ValueError, cleaner._clean_single_score,input_str)








if __name__ == "__main__":
    unittest.main()
