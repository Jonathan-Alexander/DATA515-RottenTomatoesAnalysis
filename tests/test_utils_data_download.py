"""
Runs one shot tests and multiple edge cases
for the functions imported from rotten_tomatoes.utils.data_download

test_utils_data_download does not export any classes, exceptions, or functions
"""


import unittest
from unittest import mock
import os
import json

from rotten_tomatoes.utils.data_download import ( # pylint: disable=E0401
    get_kaggle_creds,
    download_kaggle_datasets,
    validate_kaggle_dataset_list
)

@mock.patch.dict(os.environ, {"KAGGLE_USERNAME": "DEFAULT", "KAGGLE_KEY": "DEFAULT"})
class TestDataDownload(unittest.TestCase):

    """
    A class used to test the rotten_tomatoes.utils.data_download module

    Please reference the docstrings in rotten_tomatoes.utils.data_download for information
    regarding the kaggle api key pre-requisties required to successfully execute the
    get_kaggle_creds and download_kaggle_datasets functions.

    Please reference doc/TestExceptions.txt for more information regarding the following tests:

    - test_download_kaggle_datasets
    - test_download_kaggle_datasets_edge2
    - test_download_kaggle_datasets_edge3

    """

    # One shot tests
    def test_get_kaggle_creds(self):
        """One shot test passes if get_kaggle_creds returns the same username and password
        in the rotten_tomatoes/kaggle.json file"""

        dummy_kaggle_json_loc = "tests/dummy_kaggle.json"
        username, password = get_kaggle_creds(dummy_kaggle_json_loc)

        with open(dummy_kaggle_json_loc, "r", encoding='utf-8') as file:
            data = json.load(file)

        username_correct = data["username"]
        password_correct = data["key"]

        self.assertTrue((username_correct == username) and (password_correct == password))

    def test_validate_kaggle_dataset_list(self):
        """validate_kaggle_dataset_list one-shot test: passes if no ValueError is thrown"""

        kaggle_dataset_list = [
            "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
            "unanimad/the-oscar-award",
        ]

        try:
            validate_kaggle_dataset_list(kaggle_dataset_list)
        except Exception: # pylint: disable=W0703
            self.fail("Exception raised unexpectedly!")


    def test_get_kaggle_creds_edge1(self):
        """get_kaggle_creds Edge test 1: invalid file location for kaggle.json, passes if
        get_kaggle_creds throws FileNotFoundError"""

        kaggle_json_loc = "rotten_tomatoes/kaggle2.json"

        self.assertRaises(FileNotFoundError, get_kaggle_creds, kaggle_json_loc)


    def test_validate_kaggle_dataset_list_edge1(self):
        """validate_kaggle_dataset_list Edge test 1: missing / in value in kaggle_dataset_list,
        passes if validate_kaggle_dataset_list throws a Value Error"""

        # the / was removed in the second term in kaggle_dataset_list
        kaggle_dataset_list = [
            "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
            "unanimadthe-oscar-award",
        ]

        self.assertRaises(
            ValueError,
            validate_kaggle_dataset_list,
            kaggle_dataset_list,
        )

    def test_validate_kaggle_dataset_list_edge2(self):
        """validate_kaggle_dataset_list Edge test 2: value in kaggle_dataset_list is not a string,
        passes if validate_kaggle_dataset_list throws a Attribute Error"""

        # integer passed instead of string
        kaggle_dataset_list = [
            "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
            1234,
        ]

        self.assertRaises(
            AttributeError,
            validate_kaggle_dataset_list,
            kaggle_dataset_list,
        )

    @unittest.skip("Kaggle API key is required to download the data. Time intensive test.")
    def test_download_kaggle_datasets(self):
        """One shot test passes if download_kaggle_datasets downloads the following files
        to the data_download_test_data directory:
        'rotten_tomatoes_critic_reviews.csv', 'rotten_tomatoes_movies.csv', 'the_oscar_award.csv'"""

        username, password = get_kaggle_creds("rotten_tomatoes/kaggle.json")

        output_loc = "data_download_test_data/"

        kaggle_dataset_list = [
            "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
            "unanimad/the-oscar-award",
        ]

        download_kaggle_datasets(username, password, kaggle_dataset_list, output_loc)

        file_names = os.listdir(output_loc)

        files_to_check_for = [
            "rotten_tomatoes_critic_reviews.csv",
            "rotten_tomatoes_movies.csv",
            "the_oscar_award.csv",
        ]

        self.assertTrue(all(file in file_names for file in files_to_check_for))

    # Edge Tests
    @unittest.skip("Kaggle API key is required to download the data. Time intensive test")
    def test_download_kaggle_datasets_edge2(self):
        """download_kaggle_datasets Edge test 2: invalid username/dataset returns 403 error,
        passes if download_kaggle_datasets throws a Value Error"""

        with open("rotten_tomatoes/kaggle.json", "r", encoding='utf-8') as file:
            data = json.load(file)

        username = data["username"]
        password = data["key"]

        output_loc = "data_download_test_data/"

        # stefanoleone9923 is not the username associated with
        # rotten-tomatoes-movies-and-critic-reviews-dataset
        kaggle_dataset_list = [
            "stefanoleone9923/rotten-tomatoes-movies-and-critic-reviews-dataset",
            "unanimad/the-oscar-award",
        ]

        self.assertRaises(
            ValueError,
            download_kaggle_datasets,
            username,
            password,
            kaggle_dataset_list,
            output_loc,
        )

    @unittest.skip("Kaggle API key is required to download the data. Time intensive test. "
                 "Kaggle API will allow you to authenticate and download "
                 "the datasets if you enter an invalid username/password "
                 "but valid session cookie. This test will pass if you run "
                 "it by itself, but will fail if you run it in conjunction "
                 "with the other test_download_kaggle_datasets tests")
    def test_download_kaggle_datasets_edge3(self):
        """download_kaggle_datasets Edge test 3: invalid username and password combination,
        passes if download_kaggle_datasets throws a ValueError"""

        username = "madeupusername"
        password = "brokenpassword"

        output_loc = "data_download_test_data/"
        kaggle_dataset_list = [
            "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
            "unanimad/the-oscar-award",
        ]

        with self.assertRaises(ValueError):
            download_kaggle_datasets(username, password, kaggle_dataset_list, output_loc)


if __name__ == "__main__":
    unittest.main()
