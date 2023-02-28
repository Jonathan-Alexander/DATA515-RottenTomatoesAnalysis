"""
Runs 2 x one shot tests and multiple edge cases
for the functions imported from rotten_tomatoes.download_data

tests_data_download does not export any classes, exceptions, or functions
"""


import unittest
import os
import json

from rotten_tomatoes.utils.data_download import (
    get_kaggle_creds,
    download_kaggle_datasets,
)


class TestDataDownload(unittest.TestCase):

    """
    A class used to test the rotten_tomatoes.data_download module

    Please reference the docstrings in the rotten_tomatoes.data_download for information regarding the kaggle api key pre-requisties required to successfully execute the get_kaggle_creds and download_kaggle_datasets functions.

    ...

    Methods
    -------
    test_get_kaggle_creds(self)
        Tests data_download.get_kaggle_creds function to make sure it returns the username and password from a kaggle.json file saved in the rotten_tomatoes directory
    test_download_kaggle_datasets(self)
        Tests data_download.download_kaggle_dataset function to make sure it downloads the rotten tomatoes and oscars datasets correctly
    test_download_kaggle_datasets_edge1(self)
        Missing / in value in kaggle_dataset_list, passes if download_kaggle_datasets throws a Value Error
    test_download_kaggle_datasets_edge2(self)
        Invalid username/dataset format, returns 403 error, passes if download_kaggle_datasets throws a Value Error
    test_download_kaggle_datasets_edge3(self)
        Invalid username and password combination, passes if download_kaggle_datasets throws a ValueError
    test_get_kaggle_creds_edge1(self)
        Invalid file location for kaggle.json, passes if get_kaggle_creds throws FileNotFoundError

    """

    # One shot tests
    def test_get_kaggle_creds(self):
        """One shot test passes if get_kaggle_creds returns the same username and password in the rotten_tomatoes/kaggle.json file"""
        username, password = get_kaggle_creds("rotten_tomatoes/kaggle.json")

        with open("rotten_tomatoes/kaggle.json", "r") as f:
            data = json.load(f)

        username_correct = data["username"]
        password_correct = data["key"]

        status = username_correct == username and (password_correct == password)

        self.assertTrue(status)

    # @unittest.skip("skipping the successful download test")
    def test_download_kaggle_datasets(self):
        """One shot test passes if download_kaggle_datasets downloads the following files to the data_download_test_data directory: 'rotten_tomatoes_critic_reviews.csv', 'rotten_tomatoes_movies.csv', 'the_oscar_award.csv'"""
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

        downloaded_correctly = all(file in file_names for file in files_to_check_for)

        self.assertTrue(downloaded_correctly)

    # Edge Tests
    def test_download_kaggle_datasets_edge1(self):
        """download_kaggle_datasets Edge test 1: missing / in value in kaggle_dataset_list, passes if download_kaggle_datasets throws a Value Error"""
        with open("rotten_tomatoes/kaggle.json", "r") as f:
            data = json.load(f)

        username = data["username"]
        password = data["key"]

        output_loc = "data_download_test_data/"

        # the / was removed in the second term in kaggle_dataset_list
        kaggle_dataset_list = [
            "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
            "unanimadthe-oscar-award",
        ]

        self.assertRaises(
            ValueError,
            download_kaggle_datasets,
            username,
            password,
            kaggle_dataset_list,
            output_loc,
        )

    def test_download_kaggle_datasets_edge2(self):
        """download_kaggle_datasets Edge test 2: invalid username/dataset returns 403 error, passes if download_kaggle_datasets throws a Value Error"""
        with open("rotten_tomatoes/kaggle.json", "r") as f:
            data = json.load(f)

        username = data["username"]
        password = data["key"]

        output_loc = "data_download_test_data/"

        # stefanoleone9923 is not the username associate with rotten-tomatoes-movies-and-critic-reviews-dataset
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

    @unittest.skip("skipping the download_kaggle_datasets Edge test 3")
    def test_download_kaggle_datasets_edge3(self):
        """download_kaggle_datasets Edge test 3: invalid username and password combination, 
        passes if download_kaggle_datasets throws a ValueError"""
        with open("rotten_tomatoes/kaggle.json", "r") as f:
            data = json.load(f)

        username = data["username"]
        password = data["key"] + "abc123"

        output_loc = "data_download_test_data/"

        # stefanoleone9923 is not the username associate with rotten-tomatoes-movies-and-critic-reviews-dataset
        kaggle_dataset_list = [
            "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
            "unanimad/the-oscar-award",
        ]

        with self.assertRaises(ValueError):
            download_kaggle_datasets(username, password, kaggle_dataset_list, output_loc)


    def test_get_kaggle_creds_edge1(self):
        """get_kaggle_creds Edge test 1: invalid file location for kaggle.json, passes if get_kaggle_creds throws FileNotFoundError"""

        kaggle_json_loc = "rotten_tomatoes/kaggle2.json"

        self.assertRaises(FileNotFoundError, get_kaggle_creds, kaggle_json_loc)


if __name__ == "__main__":
    unittest.main()
