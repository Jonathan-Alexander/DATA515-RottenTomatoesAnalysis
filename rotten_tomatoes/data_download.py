
import os
import json



# Pre-Requisite 1: pip install kaggle


# Pre-Requisite 2a: kaggle.json file created using the instructions 
# included in the Authentication section of this website:
# https://www.kaggle.com/docs/api


# Pre-Requisite 2b: Save the kaggle.json file in the src folder
# .gitignore file includes rotten_tomatoes/kaggle.json

def get_kaggle_creds(kaggle_json_file_loc):

    print("in get_kaggle_creds")

    with open(kaggle_json_file_loc, "r") as f:
        data = json.load(f)

    username = data['username']
    password = data['key']

    print("username: ", username, "password", password)

    return username, password



def download_kaggle_dataset(username, password, kaggle_dataset, file_output): 
    print("**** in download_kaggle_dataset")

    os.environ['KAGGLE_USERNAME'] = username
    os.environ['KAGGLE_KEY'] = password  

    from kaggle.api.kaggle_api_extended import KaggleApi
    import kaggle

    split_kaggle_dataset = kaggle_dataset.split('/')
    print("split_kaggle_dataset: ", split_kaggle_dataset)

    # if(split_kaggle_dataset.len) != 2:
    #     raise ValueError("Oops! the kaggle_dataset parameter needs to be in the format username/dataset")
    
    api = KaggleApi()
    api.authenticate()

    response = kaggle.api.dataset_download_files(kaggle_dataset, path = file_output, unzip = True)
    print("&&&&&& response &&&&&&", response)

    return True
