# Background / Research Questions
1. Historically, how well have rotten tomatoes critic scores correlated with “Best movie” Oscar wins? Stretch goal: Also look at audience scores.
2. Historically, are rotten tomatoes ratings good predictors of wins in any category at the Oscars?
3. Which critics are most accurate at predicting Oscar success?

# User stories 
## Non-technical User: Someone with no technical experience at all - either software engineering or machine learning, but who is interested in the answers to our research questions.

* Needs/Wants: 
    * Answers to the research questions are immediately available. 
* Interaction methods: 
    * Point and click for results 
* Skills: 
    * None

## Technical User: Someone without experience in machine learning, but maybe some software engineering, who is interested in the answers to our research questions
* Needs/Wants: 
    * Clear documentation and repository structure, so it’s easy to find answers. 
    * Answers to the research questions are immediately available. 
    * Explainability in ML code
* Interaction methods: 
    * Command line/Run code in IDE
    * Point and click for results 
* Skills: 
    * Skilled in basic software engineering, including command-line interfaces

## Peer Reviewer: Machine learning specialist who is interested in the implementation of our regressions. May want to copy our model or processing code, or extend the research. 
* Needs/Wants: 
    * Clear documentation and repository structure, so it’s easy to find answers. 
    * Answers to the research questions are immediately available. 
    * Explainability in ML code
    * Needs to be more in depth than users. Need a readme going into model development, failed experiments, etc. etc. 
    * Would not want “simple” user experience to dominate. Make it easy to find technical details right away. 
* Interaction methods: 
    * Command line/Run code in IDE
    * Point and click for results 
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
    * Command line/Run code in IDE
* Skills: 
    * Skilled in basic software engineering, including command-line interfaces
    * Understands machine learning and model development. 

# Data Sources 

[Rotten Tomatoes Dataset](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_movies.csv)

[Oscars Dataset](https://www.kaggle.com/datasets/unanimad/the-oscar-award)


# Use Cases: 
## View model results
1. User navigates to github repository 
2. User views research results in main README of github repository. The README explains each of the questions and provides supporting graphs for the answers. 

## Review code that produced results 
1. User navigates to github repository 
2. Main README has a hyperlinked table of contents that provides quick links to code. 
3. User clicks on the link to the code they want to examine
4. User downloads repository and reviews the code. 

## Rerun entire pipeline to refresh results 
1. User navigates to github repository
2. User reviews process documentation in README file under “rotten_tomatoes” folder
3. User follows this process to rerun code. 
4. User pushes results to github. 