# How to Run the Pipeline

## Step 1: Clone the Repository
* $ git clone https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis
* RESULT: clones git repository into local environment

## Step 2: Set up Virtual Environment
* $ conda env update -f environment.yml
* RESULT: updates local environment to match project environment

## Step 3: Navigate to Root
* $ cd DATA515-RottenTomatoesAnalysis/rotten-tomatoes
* RESULT: navigates to root directory of project

## Step 4: Download the Data
* $ python data_download.py:
    * RESULT: downloads 3 kaggle datasets to data directory:
        * rotten_tomatoes_critic_reviews.csv
        * rotten_tomatoes_movies.csv
        * the_oscar_award.scv
    * NOTE: The following requirements must be satisfied before running download_data.py:
        * Pre-Requisite 1: kaggle installed in local environment. Installation instructions included here: https://www.kaggle.com/docs/api
        * Pre-Requisite 2a: kaggle.json file created using the instructions included in the Authentication section of this website: https://www.kaggle.com/docs/api
        * Pre-Requisite 2b: Save the kaggle.json file. Can be saved in the rotten_tomatoes folder, or anywhere on local machine. ().gitignore file includes rotten_tomatoes/kaggle.json)

## Step 5: Clean the Data
* $ python data_cleaning.py
    * RESULT: cleans and joins 3 datasets into full_data.csv in data directory

## Step 6: Initialize the Jupyter Notebooks
* q1_modeling.ipynb - Historically, how well have rotten tomatoes critic scores correlated with “Best movie” Oscar wins?
    * $ jupyter notebook q1_modeling.ipynb
* q2_modeling.ipynb - Historically, are rotten tomatoes ratings good predictors of wins in any category at the Oscars?
    * $ jupyter notebook q2_modeling.ipynb
* RESULT: opens jupyter notebook on local machine to be rerun or modified

## Step 7: Run the Code
* Once the notebook of interest is open, run all cells to obtain updated model

## Step 8: Push New Results to Git Repository
* $ git add q1_modeling.ipynb (or whichever notebook has been rerun or modified)
* $ git commit q1_modeling.ipynb
* $ git push
* RESULT: updated results published to git repository

