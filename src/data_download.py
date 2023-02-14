
import os
import json

# Pre-Requisite 1: pip install kaggle


# Pre-Requisite 2a: kaggle.json file created using the instructions 
# included in the Authentication section of this website:
# https://www.kaggle.com/docs/api


# Pre-Requisite 2b: Save the kaggle.json file in the src folder
# .gitignore file includes src/kaggle.json

with open("./src/kaggle.json", "r") as f:
    data = json.load(f)


os.environ['KAGGLE_USERNAME'] = data["username"]
os.environ['KAGGLE_KEY'] = data["key"]

# Uncomment the two lines of code below if you would rather 
# manually enter your Kaggle username and apikey

# os.environ['KAGGLE_USERNAME'] = "manually_enter_username"
# os.environ['KAGGLE_KEY'] = "manually_enter_apiKey"

import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi


api = KaggleApi()
api.authenticate()

kaggle.api.dataset_download_files("stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset", path ="./data/", unzip = True)

