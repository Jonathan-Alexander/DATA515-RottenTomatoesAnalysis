# Rotten Tomatoes Analysis Project
This project uses logistic regression models and statistical analysis methods to investigate the relationship between Rotten Tomatoes review scores and Oscar wins.

## Project Overview

### What data was used in this analysis?
[Rotten Tomatoes Dataset](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_movies.csv)  

[Oscars Dataset](https://www.kaggle.com/datasets/unanimad/the-oscar-award)

### What questions does this analysis address? 
1. Historically, how well have rotten tomatoes critic scores correlated with “Best movie” Oscar wins? 
2. Historically, are rotten tomatoes ratings good predictors of wins in any category at the Oscars?

### What are the possible use cases for this analysis?
[Use Cases](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/doc/functional_specification.md#use-cases)

### How do I re-run this pipeline? 
[How to Run the Pipeline](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/doc/how_to_run_pipeline.md#how-to-run-the-pipeline)

### Where can I find the final analysis?
[Question 1](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/rotten_tomatoes/q1_modeling.ipynb)  

[Question 2](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/rotten_tomatoes/q2_modeling.ipynb)

## Results 
### Question 1:  



### Question 2:

## Ideas for Future Work
The analysis contained in this repository only scratches the surface of what can be discovered with this data. Here are some potential questions for future research:
 * Which Oscar award most strongly correlates with Rotten Tomatoes scores?
 * Is there an interaction effect between genre and Rotten Tomatoes score on Oscar wins?
 * How closely do audience scores correlate with critic scores?
 * Historically, which critics have most accurately predicted Oscar success?
 * How do outside factors (budget, box office sales, etc.) affect Oscar win probability?



## File Structure

```
.
├── data
|   ├── rotten_tomatoes_critic_reviews.csv
|   ├── rotten_tomatoes_movies.csv
|   ├── the_oscar_award.csv
|   └── full_data.csv
├── doc
|   ├── img
|       ├── Data_Flow_Pipeline.png
|   ├── component_specification.md
|   ├── functional_specification.md
|   ├── how_to_run_pipeline.md
|   └── milestones.md
├── images
├── rotten_tomatoes
|   ├── utils
|       ├── __init__.py
|       ├── data_cleaning.py
|       ├── data_download.py
|       ├── regression.py
|   ├── data_cleaning.py
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
```


