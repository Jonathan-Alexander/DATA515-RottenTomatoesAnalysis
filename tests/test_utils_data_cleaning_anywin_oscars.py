"""
Runs a smoke test, multiple one shot tests and multiple edge tests
for the functions imported from utils.data_cleaning module

test_utils_data_cleaning does not export any classes, exceptions, or functions
"""


import unittest
import pandas as pd

from rotten_tomatoes.utils.data_cleaning import ( # pylint: disable=E0401
    OscarsDataCleaner,
    AnyWinOscarsDataCleaner
)


class TestUtilsDataCleaningAnyWinOscars(unittest.TestCase):
    """ A class used to test the rotten_tomatoes.utils.data_cleaning module """

    # Smoke test
    def test_smoke_cleaner(self):
        """Smoke test passes if the class initializes."""
        self.assertIsInstance(AnyWinOscarsDataCleaner(), OscarsDataCleaner)

    # One shot tests (base tests)
    #@unittest.skip("need to edit")
    def test_clean_validate_anywin_oscars(self):
        """Test passes if the _clean method correctly calculates the num_wins column
        and _verify method executes without errors """
        cleaner_aw_oscars = AnyWinOscarsDataCleaner()

        cleaner_aw_oscars.keep_columns = ["year_film", "category", "film", "winner"]

        dfs_to_test = [

            ({'year_film': [1998, 2010, 2010, 2010],
             'category': [
                "BEST MOTION PICTURE",
                "Best Actress",
                "BEST PICTURE",
                "Best Actor"
            ],
             'film': [
                "MovieABC",
                "Greatest Movie Ever",
                "Greatest Movie Ever",
                "Greatest Movie Ever"
            ],
             'winner':[False, True, True, True],
            },
            {
            'year_film':[1998, 2010],
            'film':["MovieABC", "Greatest Movie Ever"],
            'num_wins': [0, 3]
            })

        ]

        for data, exp_output in dfs_to_test:
            flag = False

            input_df =pd.DataFrame(data)
            cleaned = cleaner_aw_oscars._clean(input_df)
            exp_output_df = pd.DataFrame(exp_output)
            clean_flag = cleaned.equals(exp_output_df)
            self.assertTrue(clean_flag)
            
            cleaner_aw_oscars._validate(cleaned)

            flag = True

            self.assertTrue(flag)


if __name__ == "__main__":
    unittest.main()
