"""
Runs a smoke test, multiple one shot tests and an edge test
for the functions imported from utils.data_cleaning.MoviesDataCleaner class

test_utils_data_cleaning_movies does not export any classes, exceptions, or functions
"""


import unittest
import pandas as pd

from rotten_tomatoes.utils.data_cleaning import ( # pylint: disable=E0401
    DataCleaner,
    MoviesDataCleaner,
    ValidationException
)


class TestUtilsDataCleaningMovies(unittest.TestCase):
    """ A class used to test the rotten_tomatoes.utils.data_cleaning.MoviesDataCleaner class """

    # Smoke test
    def test_smoke_cleaner(self):
        """Smoke test passes if the class initializes."""
        self.assertIsInstance(MoviesDataCleaner(), DataCleaner)

    # One shot tests (base tests)
    def test_clean_movies(self):
        """Test passes if the _clean function removes rows with None
        in the audience rating and tomatometer_rating columns """
        cleaner_movies = MoviesDataCleaner()

        dfs_to_test = [

            ({'rotten_tomatoes_link': [1, 2, 3],
             'movie_title': [4, 5, 6],
             'tomatometer_rating': [70.0, 80.0, 90.5],
             'audience_rating':[10.0, None, "12"],
            }, 2),

            ({'tomatometer_rating':[None, 11, 12],
             'audience_rating': [None, None, "10/10"]
            }, 1),

            ({'tomatometer_rating':[70, 11, 12],
             'audience_rating': [75.0, 9.0, "10/10"]
            }, 3),

        ]

        for data, numrows in dfs_to_test:
            input_df =pd.DataFrame(data)
            self.assertEqual(cleaner_movies._clean(input_df).shape[0], numrows) # pylint: disable=W0212

    def test_validate_movies(self):
        """Passes if no error thrown by _validate"""

        cleaner_movies = MoviesDataCleaner()

        flag = False

        df_to_test = {'rotten_tomatoes_link': [1, 2, 3],
             'movie_title': ["ABC123", "Gone with the Wind", 6],
             'tomatometer_rating':[100.0, 95.0, 85.0],
             'audience_rating': [98.0, 85.0, 100.0]
            }


        input_df =pd.DataFrame(df_to_test)
        cleaner_movies._validate(input_df) # pylint: disable=W0212

        flag = True
        self.assertTrue(flag)


    # Edge tests
    def test_validate_edge(self):
        """Passes if Validation  Exeption thrown by _validate """

        cleaner_movies = MoviesDataCleaner()

        cleaner_movies.keep_columns = [
            "rotten_tomatoes_link",
            "movie_title",
            "tomatometer_rating",
            "audience_rating",
        ]

        dfs_to_test = [
            {'rotten_tomatoes_link': [1, 2, 3],
             'tomatometer_rating': [7, 8, 9],
            },

            {'movie_title': ["ABC123", "Gone with the Wind", 6],
             'audience_rating': [100.0, 85.0, 75.0]
            },

            {'rotten_tomatoes_link': [1, 2, 3],
             'movie_title': ["ABC123", "Gone with the Wind", 6],
             'tomatometer_rating':[None, 95.0, 85.0],
             'audience_rating': [98.0, 85.0, 100.0]
            },
            {'rotten_tomatoes_link': [1, 2, 3],
             'movie_title': ["ABC123", "Gone with the Wind", 6],
             'tomatometer_rating':[85.0, 95.0, 85.0],
             'audience_rating': [98.0, None, 100.0]
            },
            {'rotten_tomatoes_link': [1, 2, 3],
             'movie_title': ["ABC123", "Gone with the Wind", 6],
             'tomatometer_rating':[85.0, "A+", 85.0],
             'audience_rating': [98.0, 85.0, 100.0]
            },
            {'rotten_tomatoes_link': [1, 2, 3],
             'movie_title': ["ABC123", "Gone with the Wind", 6],
             'tomatometer_rating':[85.0, 85.0, 85.0],
             'audience_rating': [98.0, 85.0, "A-"]
            },
        ]

        for data in dfs_to_test:
            input_df =pd.DataFrame(data)
            self.assertRaises(ValidationException, cleaner_movies._validate, input_df) # pylint: disable=W0212

if __name__ == "__main__":
    unittest.main()
