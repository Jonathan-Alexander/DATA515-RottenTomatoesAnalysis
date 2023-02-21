# Rotten Tomatoes Analysis Project

## Project Type: Analysis

## Questions of Interest

1. Historically, how well have rotten tomatoes critic scores correlated with “Best movie” Oscar wins? Stretch goal: Also look at audience scores.

2. Historically, are rotten tomatoes ratings good predictors of wins in any category at the Oscars?

3. Which critics are most accurate at predicting Oscar success? (stretch goal)

<br>

## Planned File Structure

```
.
├── data
|   ├── raw
|       ├── rotten_tomatoes_critic_reviews.csv
|       ├── rotten_tomatoes_movies.csv
|       └── the_oscar_award.csv
|   └── prepped
|        └── full_data.csv
├── doc
|   ├── functional_specification.md
|   ├── component_specification.md
|   └── how_to_run_pipeline.md
├── examples
├── images
├── rotten_tomatoes
|   ├── data_cleaning.py
|   ├── data_download.py
|   ├── q1_modeling.ipynb
|   ├── q2_modeling.ipynb
|   ├── q3_modeling.ipynb (stretch goal)
|   └── utils.py
├── tests
|   ├── test_data_cleaning.py
|   ├── test_data_download.py
|   └── test_utils.py
├── LICENSE
└── README.md
└── setup.py
└── .gitignore
```

## Goals for Project Output

1. A final report as the HTML copy of the Modeling.ipynb jupyter notebook

2. Final slides for the presentation.

<br>

## Data Sources

[Rotten Tomatoes Dataset](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_movies.csv)

[Oscars Dataset](https://www.kaggle.com/datasets/unanimad/the-oscar-award)
