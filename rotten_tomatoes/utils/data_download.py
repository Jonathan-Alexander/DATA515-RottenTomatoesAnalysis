"""
Authenticates with the Kaggle API and downloads Kaggle datasets

Notes:
Pre-Requisite 1: kaggle installed in local environment.
Installation instructions included here: https://www.kaggle.com/docs/api

Pre-Requisite 2a: kaggle.json file created using the instructions included
in the Authentication section of this website: https://www.kaggle.com/docs/api

Pre-Requisite 2b: Save the kaggle.json file. Can be saved in the rotten_tomatoes folder,
or anywhere on local machine. ().gitignore file includes rotten_tomatoes/kaggle.json)


data_download exports the following functions:
    get_kaggle_creds
    validate_kaggle_dataset_list
    download_kaggle_datasets
"""
import os
import json

# pylint: disable=C0103


def get_kaggle_creds(kaggle_json_file_loc):
    """Returns a username and password (key) from kaggle.json file

    Parameters
    ----------
    kaggle_json_file_loc : string
        File location for where the kaggle.json file is saved

    Returns
    -------
    username : string
        Kaggle username
    password : string
        Kaggle password (key)
    """
    try:
        with open(kaggle_json_file_loc, "r") as f:  # pylint: disable=W1514
            data = json.load(f)
    except FileNotFoundError as e:
        raise e

    username = data["username"]
    password = data["key"]

    return username, password

def validate_kaggle_dataset_list(kaggle_dataset_list):
    """Validates username/dataset format for every string in kaggle_dataset_list

    Parameters
    ----------
    kaggle_dataset_list : list
        List of kaggle datasets to download.
        Each string in the list needs to be in "username/dataset" format

    ValueError
        - Any of the strings in the kaggle_dataset_list
            are not in the username/dataset format
    
    AttributeError
        - Any of the values in kaggle_dataset_list is not a string
    """  
    # Check each kaggle_dataset in the kaggle_dataset_list for username/dataset format
    for kaggle_dataset in kaggle_dataset_list:

        if not isinstance(kaggle_dataset, str):
            raise AttributeError(f"Oops! the kaggle_dataset parameter {kaggle_dataset}"
                                 "is not a string")
        split_kaggle_dataset = kaggle_dataset.split("/")

        if (len(split_kaggle_dataset)) != 2:
            raise ValueError(
                f"Oops! the kaggle_dataset parameter {kaggle_dataset}"
                "needs to be in the format username/dataset"
            )

def download_kaggle_datasets(username, password, kaggle_dataset_list, file_output):
    """Downloads all files from kaggle_dataset_list to the file_output location

    Parameters
    ----------
    username : string
        Kaggle username
    password : string
        Kaggle password (key)
    kaggle_dataset_list : list
        List of kaggle datasets to download.
        Each string in the list needs to be in "username/dataset" format
    file_output : string
        String for location where downloaded files should be saved.
        Recommend saving in data/ directory

    ValueError
        - Any of the strings in the kaggle_dataset_list
            are not in the username/dataset format
        - Any of the strings in the kaggle_dataset_list
            return 403 error from the kaggle.api.dataset_download_files api call


    """
    os.environ["KAGGLE_USERNAME"] = username
    os.environ["KAGGLE_KEY"] = password

    # DO NOT MOVE THIS IMPORT STATEMENT TO THE TOP OF THE FILE
    # When these import statements run, they look for kaggle.json
    # in locations listed in the Kaggle documentation https://www.kaggle.com/docs/api
    # Reference from Kaggle documentation: "the tool will look for this
    # token at ~/.kaggle/kaggle.json on Linux, OSX, and other UNIX-based operating systems,
    # and at C:\Users<Windows-username>.kaggle\kaggle.json on Windows"
    # DO NOT MOVE THIS IMPORT STATEMENT TO THE TOP OF THE FILE

    # pylint: disable=E0611
    from kaggle.api.kaggle_api_extended import KaggleApi  # pylint: disable=C0415
    import kaggle  # pylint: disable=C0415

    api = KaggleApi()
    api.authenticate()

    validate_kaggle_dataset_list(kaggle_dataset_list)

    # If all kaggle_datasets in the kaggle_dataset_list are correct, download the files
    for kaggle_dataset in kaggle_dataset_list:
        try:
            kaggle.api.dataset_download_files(
                kaggle_dataset, path=file_output, unzip=True
            )
        except Exception as e:
            raise ValueError(  # pylint: disable=W0707
                f"Oops! the kaggle_dataset {kaggle_dataset} returned an exception. {e}"
                "\nEither the username/dataset in the kaggle_dataset_list is incorrect "
                "or the username and password is incorrect. Please check both."
            )

    return True
