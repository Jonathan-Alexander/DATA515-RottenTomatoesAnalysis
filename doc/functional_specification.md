# Background / Research Questions
1. Historically, how well have rotten tomatoes critic scores correlated with “Best movie” Oscar wins? 
2. Historically, are rotten tomatoes ratings good predictors of wins in any category at the Oscars?


# User stories 
## Non-technical User: Someone with no technical experience at all who is interested in the answers to our research questions

* Needs/Wants: 
    * Answers to the research questions immediately available
* Interaction methods: 
    * Point and click for [results](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/Results.md#rotten-tomatoes-and-the-oscars-a-data-analysis-project) 
* Skills: 
    * None

## Technical User: Someone without experience in machine learning, but some in software engineering, who is interested in the answers to our research questions
* Needs/Wants: 
    * Clear documentation and repository structure, so it’s easy to find answers
    * Answers to the research questions immediately available 
    * Explainability in ML code
* Interaction methods: 
    * [Command line/Run code in IDE](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/examples/how_to_run_pipeline.md)
    * Point and click for [results](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/Results.md#rotten-tomatoes-and-the-oscars-a-data-analysis-project) 
* Skills: 
    * Skilled in basic software engineering, including command-line interfaces

## Peer Reviewer: Machine learning specialist who is interested in the implementation of our regressions. May want to copy our model or processing code, or extend the research. 
* Needs/Wants: 
    * Clear documentation and repository structure, so it’s easy to find answers. 
    * Answers to the research questions immediately available
    * Explainability in ML code
    * Needs to be more in depth than most users. Needs documentation on model development, failed experiments, etc. 
    * Does not want “simple” user experience to dominate. Must be easy to find technical details right away. 
* Interaction methods: 
    * [Command line/Run code in IDE](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/examples/how_to_run_pipeline.md)
    * Point and click for [results](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/Results.md#rotten-tomatoes-and-the-oscars-a-data-analysis-project) 
* Skills: 
    * Skilled in basic software engineering, including command-line interfaces
    * Understands basic machine learning and model development. 

## Maintainer: Machine learning specialist who is implemented in retraining and maintaining our regressions
* Needs/Wants: 
    * Clear documentation on: 
        * What order code should be run in
        * How to download data
        * How to clean data 
        * How to update model / public facing results 
* Interaction methods: 
    * [Command line/Run code in IDE](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/examples/how_to_run_pipeline.md)
* Skills: 
    * Skilled in basic software engineering, including command-line interfaces
    * Understands machine learning and model development. 

# Data Sources 

[Rotten Tomatoes Dataset](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_movies.csv)

[Oscars Dataset](https://www.kaggle.com/datasets/unanimad/the-oscar-award)


# Use Cases: 
## View model results
1. [View research results here](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/Results.md#rotten-tomatoes-and-the-oscars-a-data-analysis-project)

## Review code that produced results 
1. [View Jupyter Notebook for question 1 here](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/rotten_tomatoes/q1_modeling.ipynb) 
2. [View Jupyter Notebook for question 2 here](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/rotten_tomatoes/q2_modeling.ipynb)
3. [View main code directory here](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/tree/main/rotten_tomatoes)
4. Clone git repository via command line to personal machine: 
```
$ git clone https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis
```

## Rerun entire pipeline to refresh results 
1. [Review process documentation here](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/examples/how_to_run_pipeline.md#how-to-run-the-pipeline)
2. Follow this process to rerun code. 
3. Push results to github. 
