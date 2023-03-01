from typing import Any, List, Optional
import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

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

class RegressionAnalysis:
    def __init__(self, X: pd.DataFrame, y: pd.DataFrame, is_categorical: bool, random_state: int = 123, test_size: float = 0.25, scaler = None) -> None:
        """
        Constructor for RegressionAnalysis
        
        Args:
           X: pd.DataFrame - Input data for regression
           y: pd.DataFrame - Response variable data
           is_categorical: bool - TRUE if the response is categorical, switches regression from linear to logistic
           random_state: int = 123 - random state to use in train_test_split
           test_size: float = 0.25  - size of test set 0-1
           
        Returns:
            None
        """
        self.X = X
        self.y = y
        self.is_categorical = is_categorical
        self.random_state = random_state
        self.test_size = test_size
        self.col_indexes = None
        
        if is_categorical:
            self.model_ = LogisticRegression(class_weight='balanced')
        else:
            self.model_ = LinearRegression()
        
        self.X_train_, self.X_test_, self.y_train_, self.y_test_ = self._train_test_split(self.X, self.y, self.random_state, self.test_size)
        
        if scaler:
            self.scaler = scaler
        
    def _train_test_split(self, X: pd.DataFrame, y: pd.DataFrame, random_state: int, test_size: float) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
        """
        Constructs train and test sets
        
        Args:
            X: pd.DataFrame - input data
            y: pd.DataFrame - response data
            random_state: int - random stats for reproducability
            test_size: float - what percent of the data to withhold for testing 0-1
            
        Returns:
            X_train - train inputs
            X_test - test inputs
            y_train - train outputs
            y_test - test outputs
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, )
        X_train = X_train.to_numpy()
        X_test = X_test.to_numpy()
        y_train = y_train.to_numpy()
        y_test = y_test.to_numpy()

        if X_train.ndim == 1:
            X_train = X_train.reshape(-1, 1)

        if X_test.ndim == 1:
            X_test = X_test.reshape(-1, 1)

        return X_train, X_test, y_train, y_test
    
    def set_X_cols(self, cols: list[str])-> None:
        """
        set a subset of columns to be used as input
        
        Args:
            cols: list[str] - list of column names to use for features in the regression
            
        Returns:
            None
        """
        self.col_indexes = [self.X.columns.get_loc(c) for c in cols]
    
    def X_train(self) -> np.ndarray:
        """Returns the training input data"""
        return self.X_train_[:, self.col_indexes]
    
    def X_test(self) -> np.ndarray:
        """Returns the testing input data"""
        return self.X_test_[:, self.col_indexes]

    def fit_train(self) -> None:
        """
        Fits the model (Linear or Logistic)
        using the supplied columns, or all the columns in X if not given
        
        Args:
            None
        Returns:
            None
        """
        self.model_ = self.model_.fit(self.scaler.fit_transform(self.X_train()), self.y_train_)
        return
    
    def predict_test(self) -> np.ndarray:
        """Returns the models predictions on the testing input"""
        return self.model_.predict(self.scaler.transform(self.X_test()))
    
    def score_test(self) -> np.ndarray:
        """Returns the accuracy score for the fitted model"""
        return self.model_.score(self.scaler.transform(self.X_test()), self.y_test_)
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Returns the models predictions for a given input set
        
        Args:
            X - Input data, must dim-2 must match dim-2 of the training set
            
        Returns:
            The models predicted outut
        """
        return self.model.predict(self.scaler.transform(X))

class CorrelationAnalysis:
    
    def __init__(self, d: pd.DataFrame) -> None:
        """
        Constructor for CorrelationAnalysis
        
        Args:
            d: pd.DataFrame - input data
            
        Returns:
            None
        """
        self.data = d
        
    def corr_matrix(self, subset: list[str] = None) -> pd.DataFrame:
        """
        Returns the correlation matrix for the data
        
        Args:
            subset - list of column names to consider in the correlation matrix
            
        Returns
            DataFrame representing the correlation matrix
        """
        if subset:
            return self.data[subset].corr()
            
        return self.data.corr()
    
    def plot_heatmap(self, subset: list[str] = None) -> None:
        """
        Displays a heatmap of the correlation matrix
        
        Args:
            subset - list of column names to consider in the correlation matrix
        Returns:
            None
        """
        sns.heatmap(self.corr_matrix(subset).round(2), annot=True, vmax=1, vmin=-1)
        return
    
    def corr_coef(self, a: str, b: str) -> float:
        """
        Provides the correlation coefficient between two variables in the dataset
        
        Args:
            a - One variable to be compared
            b - The other variable
        """
        return self.data[a].corr(self.data[b])
    
'''
--------------------
OTHER UTILS
====================
'''
def plot_linear_fit(X, y_pred, y_test):
    plt.scatter(X, y_test, color='black')
    plt.scatter(X, y_pred, color='blue', marker='.')
    plt.show()