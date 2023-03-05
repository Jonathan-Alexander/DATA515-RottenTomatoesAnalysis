"""
Runs 2 x one shot tests and multiple edge cases
for the functions imported from rotten_tomatoes.download_data

tests_data_download does not export any classes, exceptions, or functions
"""


import unittest
import json

from rotten_tomatoes.utils.data_download import ( # pylint: disable=E0401
    get_kaggle_creds,
    validate_kaggle_dataset_list
)


class TestDataDownload(unittest.TestCase):

    """
    A class used to test the rotten_tomatoes.data_download module

    Please reference the docstrings in rotten_tomatoes.utils.data_download for information
    regarding the kaggle api key pre-requisties required to successfully execute the
    get_kaggle_creds and download_kaggle_datasets functions.

    ...

    Methods
    -------
    test_get_kaggle_creds(self)
        Tests data_download.get_kaggle_creds function to make sure it returns the username
        and password from a kaggle.json file saved in the rotten_tomatoes directory
    test_download_kaggle_datasets_edge1(self)
        Missing / in value in kaggle_dataset_list, passes if download_kaggle_datasets
        throws a Value Error
    test_get_kaggle_creds_edge1(self)
        Invalid file location for kaggle.json, passes if get_kaggle_creds throws FileNotFoundError
    test_validate_kaggle_dataset_list_edge2(self)
        value in kaggle_dataset_list is not a string,
        passes if validate_kaggle_dataset_list throws a Attribute Error


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

        status = (username_correct == username) and (password_correct == password)

        self.assertTrue(status)

    def test_validate_kaggle_dataset_list(self):
        """validate_kaggle_dataset_list one-shot test: passes if no ValueError is thrown"""

        kaggle_dataset_list = [
            "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
            "unanimad/the-oscar-award",
        ]

        flag = False

        validate_kaggle_dataset_list(kaggle_dataset_list)

        flag = True

        self.assertTrue(flag)


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


if __name__ == "__main__":
    unittest.main()
