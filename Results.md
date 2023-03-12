# Rotten Tomatoes and the Oscars: A Data Analysis Project

## Background

It’s hard to deny the cultural relevance of Rotten Tomatoes, a review website that aggregates critics’ ratings and calculates a score that’s either “fresh” or “rotten”. But how accurate is the self-proclaimed “most trusted measurement of quality for movies” really? Enter another cultural giant: the Oscars. Regarded by many as the most prestigious awards ceremony in the entertainment industry, the ceremony’s top prize of “Best Picture” is widely viewed as the highest honor a movie can receive. In this data analysis, we set out to discover how closely these two variables are related. Can Rotten Tomatoes scores be used as a reliable predictor of a film’s Oscar success?

## Data

This analysis is built from three Kaggle datasets: 

[rotten_tomatoes_movies.csv](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_movies.csv), which provides aggregated Rotten Tomatoes scores

[rotten_tomatoes_critic_reviews.csv](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_critic_reviews.csv), which provides individual critic reviews

[the_oscar_award.csv](https://www.kaggle.com/datasets/unanimad/the-oscar-award), which provides all historical Oscar nominations and wins 

Our pipeline downloads these three Kaggle datasets, merges them, and cleans the final merged dataset for analysis. Those interested in viewing and/or analyzing the data on their local machine should follow the process described [here](https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/examples/how_to_run_pipeline.md#how-to-run-the-pipeline).

## Results
### Historically, how well have Rotten Tomatoes critic scores correlated with “Best Picture” Oscar wins?


To find the answer to this first research question, we ran a simple logistic regression of critic rotten tomatoes score to best picture wins. When plotting the data, you see that many winning movies have low Rotten Tomatoes scores. 
<p align="center">
  <img width="460" height="300" src=https://raw.githubusercontent.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/main/images/ratings_bins_all.png>
</p>

It seemed like there might be an outlier issue, with even very popular movies getting low ratings from a few critics. For example, here are the critic ratings for the film "American Beauty", which won the best picture Oscar in 1999. 


<p align="center">
    <img width="370" height="300" src=https://github.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/blob/main/images/american_beauty_scores.png?raw=true>
</p>

So we decided to take the average of Rotten Tomatoes scores instead, which gave the following breakdown:

<p align="center">
  <img width="370" alt="bins" src="https://user-images.githubusercontent.com/122406312/224567283-6e53ff4b-232d-426a-b9a8-8e9da7b6dc51.png">
</p>

In the first runs of the model, we noticed that the model was only ever predicting losses. Therefore, we increased the class weights to ensure that the model was predicting at least one Best Picture win. We ran some hyperparameter optimization to ensure that we were picking the class weights with the highest test accuracy. 

However, even with these improvements, our best any-win model coefficient was 0.023. When the model was allowed to predict no wins, its regression coefficient was 0.028. This tells us that Rotten Tomatoes critic score is not a strong predictor of a Best Picture Oscars win. 

The highest any-win model test accuracy we saw was 83.3%, while the no-win model was 84.3%. This tells us that predicting no wins at all leads to higher performance with this model architecture. 

To improve these results, you might need to choose a more complicated model than logistic regression, or add in other explanatory variables. 

### Are Rotten Tomatoes scores a good predictor of Oscars success?

To answer this second question we first define “Oscars success”. We defined Oscar
success in two ways. Firstly, winning an award at the Oscars, this definition is simply true or false depending on if the film won any award at the Oscars. Secondly, we defined success in terms of the number of awards a film won at the Oscars, with more awards being more success.

<p align="center">
  <img width="370" alt="boxplot" src="https://user-images.githubusercontent.com/122406312/224567289-e3c28fcf-dd76-4a45-8966-098846f362cd.png">
</p>

Looking at the distribution of ratings across levels of Oscar’s success it initially appeared as though Rotten Tomatoes critic reviews may be predictive of Oscar’s success.

With these definitions we conducted correlation and regression analysis. Looking at our correlation analysis we found that the average critic score was not highly correlated with either the number of awards won nor general success. Below is a heatmap showing this analysis as well as a few other metrics we investigated.

<p align="center">
  <img width="370" alt="Heatmap" src="https://user-images.githubusercontent.com/122406312/224566980-8a1ec6ac-be6f-4f90-a834-df77bed91b69.png">
</p>

We then investigated a causal relationship between Rotten Tomatoes scores and Oscars success along the same two definitions. To do this we utilized linear regression analysis. Below is a plot of the linear fit between average critic rating and the number of awards a movie won at the Oscars. 

<p align="center">
 <img width="370" height="300" src=https://raw.githubusercontent.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/main/images/oscar_wins_review_score_fit.png>
</p>

As we can see, the fit is not strong(R = 0.045). This agrees with the results of the correlation analysis. Looking closer at the fit we can see that all of the movies winning more than two awards are not covered by the fit. This is seemingly due to the large number of movies that won no awards at all ranges of the rating scale. Our other definition of success (wining any award at the Oscars) showed similar results.

<p align="center">
  <img width="370" height="300" src=https://raw.githubusercontent.com/Jonathan-Alexander/DATA515-RottenTomatoesAnalysis/main/images/oscar_success_review_score_fit.png>
</p>

In investigating the predictive power of Rotten Tomatoes scores we also considered audience ratings in addition to critic ratings.  We followed the same methodology and obtained the following fit for the number of awards won by a movie.

<p align="center">
  <img width="376" alt="Audience Score" src="https://user-images.githubusercontent.com/122406312/224566816-fa332525-937f-4854-a994-1fe43de60e52.png">
</p>


This illustrates how historically Rotten Tomatoes scores have not been a strong predictor of Oscar’s success. With the addition of the analysis into the predictive strength of audience ratings showing similar results (R = 0.032) we may also conclude that audience ratings are not strong predictors of Oscar success.

## Ideas for Further Analysis
The analysis contained in this repository only scratches the surface of what can be discovered with this data. Here are some potential questions for future research:

* Does another model type (besides logistic regression) more accurately fit the relationship between Rotten Tomatoes scores and Oscar wins?
* Which Oscar award most strongly correlates with Rotten Tomatoes scores?
* Is there an interaction effect between genre and Rotten Tomatoes score on Oscar wins?
* How closely do audience scores correlate with critic scores?
* Historically, which critics have most accurately predicted Oscar success?
* How do outside factors (budget, box office sales, etc.) affect Oscar win probability?
* Do scores from top critics correlate more strongly with Oscar wins than non-top critics?


