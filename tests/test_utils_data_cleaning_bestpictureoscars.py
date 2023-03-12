"""
Runs a smoke test and edge test for the functions imported from
rotten_tomatoes.utils.data_cleaning.BestPictureOscarsDataCleaner class

test_utils_data_cleaning_bestpictureoscars does not export any classes, exceptions, or functions
"""


import unittest
import pandas as pd

from rotten_tomatoes.utils.data_cleaning import ( # pylint: disable=E0401
    OscarsDataCleaner,
    BestPictureOscarsDataCleaner,
    ValidationException
)


class TestUtilsDataCleaningBestPictureOscars(unittest.TestCase):
    """ A class used to test the
    rotten_tomatoes.utils.data_cleaning.BestPictureOscarsDataCleaner class """

    # Smoke test
    def test_smoke_cleaner(self):
        """Smoke test passes if the class initializes."""
        self.assertIsInstance(BestPictureOscarsDataCleaner(), OscarsDataCleaner)

    # One shot tests (base tests)
    def test_clean_validate_bestpictureoscars(self):
        """Test passes if the _clean function removes rows with values other then the ones
        included in best_picture_categores in the category column """
        cleaner_bp_oscars = BestPictureOscarsDataCleaner()

        cleaner_bp_oscars.keep_columns = ["year_film", "category", "film", "winner"]

        best_picture_categories = [
            "BEST MOTION PICTURE",
            "BEST PICTURE",
            "OUTSTANDING PICTURE",
            "OUTSTANDING MOTION PICTURE",
            "Best Picture",
            "BEST MOTION PICTURE",
        ]

        dfs_to_test = [

            ({'year_film': [1998, 1999, 2000, 2010, 2015, 2022, 2005],
             'category': [
                "BEST MOTION PICTURE",
                "BEST PICTURE",
                "OUTSTANDING PICTURE",
                "OUTSTANDING MOTION PICTURE",
                "Best Picture",
                "BEST MOTION PICTURE",
                "Best Actor"
            ],
             'film': [
                "Movie_Title",
                "Greatest Movie Ever",
                "11/22/63",
                "Pirates of the Caribbean",
                "The Worst Movie",
                "Encancto",
                "The So-So Movie"
            ],
             'winner':[False, True, True, False, True, False, False],
            }, 6)

        ]

        for data, numrows in dfs_to_test:
            flag = False
            input_df =pd.DataFrame(data)
            cleaned = cleaner_bp_oscars._clean(input_df) # pylint: disable=W0212

            self.assertEqual(cleaned.shape[0], numrows)

            for value in cleaned['category']:
                self.assertTrue(value in best_picture_categories)

            cleaner_bp_oscars._validate(cleaned) # pylint: disable=W0212
            flag = True
            self.assertTrue(flag)

    # Edge test
    def test_validate_edge(self):
        """Passes if Validation Exception thrown by _validate """

        cleaner_bp_oscars = BestPictureOscarsDataCleaner()

        cleaner_bp_oscars.keep_columns = ["year_film", "category", "film", "winner"]

        dfs_to_test = [
            {
            'year_film': [1998, 2000, 2000],
            'category': [
                "BEST MOTION PICTURE",
                "BEST PICTURE",
                "OUTSTANDING PICTURE"
            ],
            'film': [
                "Movie_Title",
                "Greatest Movie Ever",
                "11/22/63",
            ],
            'winner':[False, True, True],
            },
            {
            'year_film': [1998, 1999, 2000],
            'category': [
                "BEST MOTION PICTURE",
                "BEST PICTURE",
                "OUTSTANDING PICTURE"
            ],
            'film': [
                "Movie_Title",
                "Greatest Movie Ever",
                "11/22/63"
            ],
            'winner':[False, None, True],
            }
        ]

        for data in dfs_to_test:
            input_df =pd.DataFrame(data)
            self.assertRaises(ValidationException, cleaner_bp_oscars._validate, input_df) # pylint: disable=W0212


if __name__ == "__main__":
    unittest.main()
