"""
Authenticates with the Kaggle API and downloads Kaggle datasets

Notes:
Pre-Requisite 1: kaggle installed in local environment. Installation instructions included here: https://www.kaggle.com/docs/api

Pre-Requisite 2a: kaggle.json file created using the instructions included in the Authentication section of this website: https://www.kaggle.com/docs/api

Pre-Requisite 2b: Save the kaggle.json file. Can be saved in the rotten_tomatoes folder, or anywhere on local machine. ().gitignore file includes rotten_tomatoes/kaggle.json)


data_download exports the following functions: 
    get_kaggle_creds
    download_kaggle_datasets
"""
import os
import json


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
    #print("in get_kaggle_creds")

    with open(kaggle_json_file_loc, "r") as f:
        data = json.load(f)

    username = data['username']
    password = data['key']
    #print("username: ", username, "password", password)

    return username, password



def download_kaggle_datasets(username, password, kaggle_dataset_list, file_output):
    """Downloads all files from kaggle_dataset_list to the file_output location

    Parameters
    ----------
    username : string
        Kaggle username
    password : string
        Kaggle password (key)
    kaggle_dataset_list : list
        List of kaggle dataset to download. Each string in the list needs to be in "username/dataset" format
    file_output : string
        String for location where downloaded files should be saved. Recommend saving in a data/raw directory
        
    """ 
    #print("in download_kaggle_dataset\n")

    os.environ['KAGGLE_USERNAME'] = username
    os.environ['KAGGLE_KEY'] = password

    # DO NOT MOVE THIS IMPORT STATEMENT TO THE TOP OF THE FILE
    # When these import statements run, they look for kaggle.json in locations listed in the Kaggle documentation https://www.kaggle.com/docs/api
    # Reference from Kaggle documentation: "the tool will look for this token at ~/.kaggle/kaggle.json on Linux, OSX, and other UNIX-based operating systems, and at C:\Users<Windows-username>.kaggle\kaggle.json on Windows"
    # DO NOT MOVE THIS IMPORT STATEMENT TO THE TOP OF THE FILE
    from kaggle.api.kaggle_api_extended import KaggleApi
    import kaggle

    api = KaggleApi()
    api.authenticate()

    for kaggle_dataset in kaggle_dataset_list:

        #split_kaggle_dataset = kaggle_dataset.split('/')
        #print("split_kaggle_dataset: ", split_kaggle_dataset)

        # if(split_kaggle_dataset.len) != 2:
        #     raise ValueError("Oops! the kaggle_dataset parameter needs to be in the format username/dataset")

        kaggle.api.dataset_download_files(kaggle_dataset, path = file_output, unzip = True)

    return True
