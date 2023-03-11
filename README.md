# Rotten Tomatoes Analysis Project
This project uses logistic regression models and statistical analysis methods to investigate the relationship between Rotten Tomatoes review scores and Oscar wins. It focuses on two main research questions:
1. Historically, how well have rotten tomatoes critic scores correlated with “Best picture” Oscar wins? 
2. Historically, are rotten tomatoes ratings good predictors of wins in any category at the Oscars?

## Repository Guide

### What data is used in this analysis?
This project uses two datasets available on Kaggle, a dataset of Rotten Tomatoes critic reviews and a dataset of all Oscar awards. 

[Rotten Tomatoes Dataset](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_movies.csv)  

[Oscars Dataset](https://www.kaggle.com/datasets/unanimad/the-oscar-award)

### What can I do with this repository?
[Use Cases](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/doc/functional_specification.md#use-cases)

### How do I re-run the data analysis pipeline? 
[How to run the pipeline](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/examples/how_to_run_pipeline.md#how-to-run-the-pipeline)

### Where can I find the final analysis?
[Question 1](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/rotten_tomatoes/q1_modeling.ipynb)  

[Question 2](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/rotten_tomatoes/q2_modeling.ipynb)

### Where can I find the results?
[Results](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/Results.pdf)

### Where can I find in depth component and functional documentation?
[Documentation](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/tree/main/doc)

## File Structure

```
.
├── data
|   ├── rotten_tomatoes_critic_reviews.csv
|   ├── rotten_tomatoes_movies.csv
|   ├── the_oscar_award.csv
|   ├── best_picture_data.csv
|   └── any_win_data.csv
├── doc
|   ├── img
|       ├── Data_Flow_Pipeline.png
|   ├── component_specification.md
|   ├── functional_specification.md
|   └── milestones.md
├── examples
|   ├── how_to_run_pipeline.md
├── images
|   ├── american_beauty_scores.png
|   ├── heatmap.png
|   ├── oscar_success_review_score_fit.png
|   ├── oscar_wins_review_score_fit.png
|   ├── ratings_bins_all.png
|   ├── ratings_bins_average.png
├── rotten_tomatoes
|   ├── utils
|       ├── __init__.py
|       ├── data_cleaning.py
|       ├── data_download.py
|       ├── regression.py
|   ├── data_cleaning.py
|   ├── data_download.py
|   ├── q1_modeling.ipynb
|   ├── q2_modeling.ipynb
|   └── __init__.py
├── tests
|   ├── test_data_cleaning.py
|   ├── test_data_download.py
|   └── test_utils.py
├── LICENSE
└── README.md
└── setup.py
└── .gitignore
└── environment.yml
└── __init__.py
└── .coveragerc
```

### License
This project is licensed under a MIT license. 

### About the project
This project was created for the University of Washington's DATA 515 course in Winter 2023.
The authors are Jonathan Alexander, Debbie Davis, Emily Linebarger, and Carolina Mack. 