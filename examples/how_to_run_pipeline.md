# How to Run the Pipeline

## Step 1: Clone Repository

- Execute the following from the command line

```
$ git clone https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis
```

- **RESULT:** clones git repository into local environment

<br>

## Step 2: Set up Virtual Environment

- Pre-Requisite: Anaconda installed. Installation instructions: https://docs.anaconda.com/anaconda/install/index.html

- Navigate to the cloned directory and update the conda environment by executing the following from the command line

```
$ cd DATA515-RottenTomatoesAnalysis
$ conda env update -f environment.yml
```

- Activate the conda environment by executing the following from the command line

```
$ conda activate rta
```

- **RESULT:** updates local environment to match project environment

<br>

## Step 3: Install rotten_tomatoes

- Execute the following from the command line

```
$ pip install -e .
```

- **RESULT:** Installs packages and runs setup.py

<br>

## Step 4: Download Kaggle Datasets

- Pre-Requisite 1: Create kaggle.json file using the instructions included in the Authentication section of this website: https://www.kaggle.com/docs/api

- Pre-Requisite 2: Save the kaggle.json file to the rotten_tomatoes directory.

  - If the kaggle.json file is not saved in the rotten_tomatoes directory, update the path to the kaggle.json file in the get_kaggle_creds input on line 9 of rotten_tomatoes/data_download.py.

  - .gitignore file includes rotten_tomatoes/kaggle.json

- Optional changes to rotten_tomatoes/data_download.py

  - Change datasets to download from Kaggle by changing the values in the kaggle_dataset_list variable in the rotten_tomatoes/data_download.py file

- Execute the following from the command line

  ```
  $ python rotten_tomatoes/data_download.py
  ```

- **RESULT:** downloads 3 kaggle datasets to data directory:
  - rotten_tomatoes_critic_reviews.csv
  - rotten_tomatoes_movies.csv
  - the_oscar_award.scv

<br>

## Step 5: Clean Data

- Note: If the output_loc variable on line 17 of rotten_tomatoes/data_download.py was changed, the read methods in rotten_tomatoes_utils/data_cleaning.py will also need to be updated.

  - Example: If the output_loc variable was changed to "data/temp", the data variable in the read method of the CriticsDataCleaner class would need to be changed to:

    ```
    data = pd.read_csv("./data/temp/rotten_tomatoes_critic_reviews.csv")
    ```

- Execute the following from the command line
  ```
  $ python rotten_tomatoes/data_cleaning.py
  ```
- **RESULT:** cleans and joins 3 Kaggle datasets into 2 cleaned datasets for analysis in data directory:
  - any_win_data.csv
  - best_picture_data.csv

<br>

## Step 6: Open Jupyter Notebook

- Note: Ensure the rta environment is activated before opening jupyter notebook
- Execute the following from the command line
  ```
  $ jupyter notebook
  ```
- Once jupyter notebook opens, navigate to the following jupyter notebooks in the rotten_tomatoes directory:

  - q1_modeling.ipynb - Historically, how well have rotten tomatoes critic scores correlated with “Best movie” Oscar wins?

  - q2_modeling.ipynb - Historically, are rotten tomatoes ratings good predictors of wins in any category at the Oscars?

- **RESULT**: opens jupyter notebook locally

<br>

## Step 7: Run Code

- Once the notebook of interest is open, run all cells to obtain updated model
- **RESULT** Images with model results published to images directory

<br>

## Step 8: Update Results

- Manually update the information included in Results file, including copying images from the images directory into the Results file

<br>

## Step 9: Push New Results to Git Repository

- Execute the following from the command line:

- Pre-Requisite 1: Request permission from GitHub repo owner to push changes to the repository

- Pre-Requisite 2: GitHub command line configured. Reference GitHub documentation for more information: https://docs.github.com/en/github-cli/github-cli/quickstart

- Execute the following from the command line, replace the values inside the {} with the appropriate file name. (Make sure to delete the {} characters)

```
$ git add {modified_notebook}
$ git commit {q1_modeling.ipynb}
$ git push
```

- Example: updating q1_modeling.ipynb

```
$ git add q1_modeling.ipynb
$ git commit q1_modeling.ipynb
$ git push
```

- **RESULT:** updated results published to git repository
