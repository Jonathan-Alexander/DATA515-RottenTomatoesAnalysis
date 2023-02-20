"""
Runs 2 x one shot tests, and will eventually run multiple edge cases
for the functions imported from rotten_tomatoes.download_data

tests_data_download does not export any classes, exceptions, or functions
"""


import unittest
import os
import json

from rotten_tomatoes import get_kaggle_creds, download_kaggle_datasets


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

    """

    # One shot tests
    def test_get_kaggle_creds(self):
        """ One shot test passes if get_kaggle_creds returns the same username and password in the rotten_tomatoes/kaggle.json file"""
        username, password = get_kaggle_creds("rotten_tomatoes/kaggle.json")
        #print("username: ", username, "password: ", password)

        with open("rotten_tomatoes/kaggle.json", "r") as f:
            data = json.load(f)
        
        username_correct = data['username']
        password_correct = data['key']

        status = (username_correct == username and (password_correct == password))

        self.assertTrue(status)
    
    def test_download_kaggle_datasets(self):
        """ One shot test passes if download_kaggle_datasets downloads the following files to the data_download_test_data directory: 'rotten_tomatoes_critic_reviews.csv', 'rotten_tomatoes_movies.csv', 'the_oscar_award.csv'"""
        with open("rotten_tomatoes/kaggle.json", "r") as f:
            data = json.load(f)
        
        username = data['username']
        password = data['key']

        output_loc = "data_download_test_data/"

        kaggle_dataset_list = ["stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset", "unanimad/the-oscar-award"]
        
        download_kaggle_datasets(username, password, kaggle_dataset_list, output_loc)

        file_names = os.listdir(output_loc)
        #print("Files downloaded: \n")
        #print(file_names)

        files_to_check_for = ['rotten_tomatoes_critic_reviews.csv', 'rotten_tomatoes_movies.csv', 'the_oscar_award.csv']

        downloaded_correctly = all(file in file_names for file in files_to_check_for)
        #print("\ndownloaded_correctly: ", downloaded_correctly)

        self.assertTrue(downloaded_correctly)

if __name__ == '__main__':
    unittest.main()