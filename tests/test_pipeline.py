"""
Runs 2 x one shot tests and multiple edge cases
for the functions imported from rotten_tomatoes.download_data

tests_data_download does not export any classes, exceptions, or functions
"""
import unittest
import os
import json

from rotten_tomatoes.utils.data_download import ( # pylint: disable=E0401
    get_kaggle_creds,
    download_kaggle_datasets,
)


class TestPipeline(unittest.TestCase):
    """
    A class used to test the rotten_tomatoes.data_download module

    Please reference the docstrings in rotten_tomatoes.utils.data_download for information
    regarding the kaggle api key pre-requisties required to successfully execute the
    get_kaggle_creds and download_kaggle_datasets functions.

    ...

    Methods
    -------
    test_download_kaggle_datasets(self)
        Tests data_download.download_kaggle_dataset function to make sure it downloads
        the rotten tomatoes and oscars datasets correctly
    test_download_kaggle_datasets_edge1(self)
        Missing / in value in kaggle_dataset_list, passes if download_kaggle_datasets
        throws a Value Error
    test_download_kaggle_datasets_edge2(self)
        Invalid username/dataset format, returns 403 error, passes if
        download_kaggle_datasets throws a Value Error
    test_download_kaggle_datasets_edge3(self)
        Invalid username and password combination, passes if
        download_kaggle_datasets throws a ValueError

    """

    @unittest.skip("Kaggle API key is required to download the data")
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

        downloaded_correctly = all(file in file_names for file in files_to_check_for)

        self.assertTrue(downloaded_correctly)

    # Edge Tests


    @unittest.skip("Kaggle API key is required to download the data")
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

    @unittest.skip("Kaggle API key is required to download the data")
    def test_download_kaggle_datasets_edge3(self):
        """download_kaggle_datasets Edge test 3: invalid username and password combination,
        passes if download_kaggle_datasets throws a ValueError"""
        with open("rotten_tomatoes/kaggle.json", "r", encoding='utf-8') as file:
            data = json.load(file)

        username = data["username"]
        password = data["key"] + "abc123"

        output_loc = "data_download_test_data/"

        # stefanoleone9923 is not the username associate with
        # rotten-tomatoes-movies-and-critic-reviews-dataset
        kaggle_dataset_list = [
            "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
            "unanimad/the-oscar-award",
        ]

        with self.assertRaises(ValueError):
            download_kaggle_datasets(username, password, kaggle_dataset_list, output_loc)

if __name__ == "__main__":
    unittest.main()
