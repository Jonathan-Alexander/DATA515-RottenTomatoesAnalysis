"""Runs data download steps."""

from utils.data_download import ( # pylint: disable=E0401
    get_kaggle_creds,
    download_kaggle_datasets,
)

username, password = get_kaggle_creds("rotten_tomatoes/kaggle.json")
# pylint: disable=C0103
output_loc = "data/"

kaggle_dataset_list = [
    "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset",
    "unanimad/the-oscar-award",
]

download_kaggle_datasets(username, password, kaggle_dataset_list, output_loc)
