"""Runs data download steps."""

from utils.data_download import (  # pylint: disable=E0401
    get_kaggle_creds,
    download_kaggle_datasets,
)
# Set the location for where you saved the kaggle.json file
# Reference doc strings in utils/data_download for more
# information regarding the kaggle.json file
# pylint: disable=C0103
kaggle_json_file_loc = "rotten_tomatoes/kaggle.json"

username, password = get_kaggle_creds(kaggle_json_file_loc)

# Set the location for the files downloaded from kaggle should be saved
# pylint: disable=C0103
output_loc = "data/"

# Give the list of files to download from Kaggle
# Each str in the list should be in a the username/dataset format
kaggle_dataset_list = [
    "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
    "unanimad/the-oscar-award",
]

# Download the dataset(s) from Kaggle
download_kaggle_datasets(username, password, kaggle_dataset_list, output_loc)
