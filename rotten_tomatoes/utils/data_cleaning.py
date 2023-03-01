from typing import Any, List, Optional
import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

class DataCleaner():
    """Base class. Defines interface for data cleaning."""
    keep_columns = None

    def __init__(self):
        pass

    def run(self) -> pd.DataFrame():
        """Runs all data loading and cleaning steps."""
        data = self._read()
        data = self._clean(data)
        self._validate(data)
        
        return data

    def _read(self) -> pd.DataFrame:
        raise NotImplementedError()

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError()

    def _validate(self, data: pd.DataFrame) -> None:
        for col in self.keep_columns:
            if col not in data:
                raise Exception(f"Missing {col} from data!")
    
    def _validate_rating_col(self, data: pd.DataFrame, col: str) -> None:
        if col not in data.columns:
            raise Exception(f"Column {col} not available in passed data!")
        if data.loc[data[col].isna()].shape[0] > 0:
            raise Exception(f"Null values not allowed in {col}!")
        if not all(isinstance(x, float) for x in data[col]):
            breakpoint()
            raise Exception(f"Found non-float values for {col}!")


class CriticsDataCleaner(DataCleaner):
    """Clean critics dataset."""
    keep_columns = ['rotten_tomatoes_link', 'critic_name', 'top_critic', 'review_type', 'review_score']

    def _read(self) -> pd.DataFrame:
        data = pd.read_csv('./data/rotten_tomatoes_critic_reviews.csv')
        return data[self.keep_columns]
    
    def _clean_single_score(self, score: str) -> Optional[float]:
        """Cleans a single score to a 0-100 scale."""
        substitutions = {
            'A': 90,
            'B': 80,
            'C': 70,
            'D': 60,
            'E': 50,
            'F': 40
        }
        # If score can already be converted to float, return. 
        try: 
            return float(score)
        except Exception as e:
            pass
        # Then, clean. 
        # First, take any observations with a "/" and divide them.
        if "/" in score:
            numerator, denominator = score.split("/")
            numerator = float(numerator)
            denominator = float(denominator)
            if denominator == 0:
                return None
            return (float(numerator) / float(denominator)) * 100
        
        # Handle alphanumeric case. Remove any "-" or "+" signs, 
        # and then use substitution dictionary. 
        for char in ['-', "+", " "]: 
            score = score.replace(char, "")
        
        if score not in substitutions.keys():
            raise Exception(f"Unable to process score {score}.")
        return substitutions[score]

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        1.) Subset to the columns we care about 
        2.) Because we only care about the numerical rating, drop any observations where 
            rating is null. 
        3.) Standardize review scores. 
        """
        data = data.loc[~data['review_score'].isna()]

        # Standardize review scores between 0-100. 
        # There are both numerical, ratio, and letter scores. 
        cleaned_review_scores = []
        for _, row in data.iterrows():
            cleaned_review_scores.append(self._clean_single_score(row['review_score']))
        
        data['review_score'] = cleaned_review_scores

        # Drop out any NA values from review score 
        return data.loc[~data['review_score'].isna()]

    def _validate(self, data: pd.DataFrame) -> None:
        """
        1.) Assert no null values in reviews 
        2.) Assert the 'keep_columns' are in the data 
        """
        super()._validate(data)
        self._validate_rating_col(data, 'review_score')


class MoviesDataCleaner(DataCleaner):
    """Clean movies dataset."""
    keep_columns = ['rotten_tomatoes_link', 'movie_title', 'tomatometer_rating', 'audience_rating']

    def _read(self) -> pd.DataFrame:
        data = pd.read_csv('./data/rotten_tomatoes_movies.csv')
        return data[self.keep_columns]

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        """Clean data."""
        data = data.loc[~data['tomatometer_rating'].isna()]
        data = data.loc[~data['audience_rating'].isna()]
        return data

    def _validate(self, data: pd.DataFrame) -> None:
        """
        1.) Assert no null values in tomatometer or audience rating 
        2.) Assert all rating columns between 0-100
        """
        super()._validate(data)
        self._validate_rating_col(data, 'tomatometer_rating')
        self._validate_rating_col(data, 'audience_rating')

class OscarsDataCleaner(DataCleaner):
    """Clean Oscars dataset."""
    keep_columns = ['year_film', 'year_ceremony', 'ceremony', 'category', 'name', 'film', 'winner']

    def _read(self) -> pd.DataFrame:
        data = pd.read_csv('./data/the_oscar_award.csv')
        return data[self.keep_columns]

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        """Clean data."""
        return data

    def _validate(self, data: pd.DataFrame) -> None:
        super()._validate(data)
