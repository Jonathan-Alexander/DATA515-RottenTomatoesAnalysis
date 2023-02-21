import unittest
import json
import numpy as np

from rotten_tomatoes import get_kaggle_creds, download_kaggle_dataset


class TestDataDownload(unittest.TestCase):

    # Smoke tests
    def test_get_kaggle_creds_smoke(self):
        get_kaggle_creds("rotten_tomatoes/kaggle.json")
        self.assertTrue(True)
    
    # def test_download_kaggle_dataset(self):

    #     with open("rotten_tomatoes/kaggle.json", "r") as f:
    #         data = json.load(f)
        
    #     username = data['username']
    #     password = data['key']

    #     kaggle_dataset = "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset"

    #     output_loc = "data_download_test_data/"

    #     status = download_kaggle_dataset(username, password, kaggle_dataset, output_loc)

    #     self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()