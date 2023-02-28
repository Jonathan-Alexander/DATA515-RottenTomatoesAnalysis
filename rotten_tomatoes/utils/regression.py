"""Helper classes for statistical analysis."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns

# pylint: disable=C0103,R0902


class RegressionAnalysis:
    """Helper class for regression analysis."""

    def __init__(
        self,
        X: pd.DataFrame,
        y: pd.DataFrame,
        is_categorical: bool,
        test_size: float = 0.25,
    ) -> None:
        """
        Constructor for RegressionAnalysis

        Args:
           X: pd.DataFrame - Input data for regression
           y: pd.DataFrame - Response variable data
           is_categorical: bool - 
            TRUE if the response is categorical, 
            switches regression from linear to logistic
           test_size: float = 0.25  - size of test set 0-1

        Returns:
            None
        """
        self.X = X
        self.y = y
        self.is_categorical = is_categorical
        self.test_size = test_size

        self.col_indexes = None
        self.random_state = 123

        if is_categorical:
            self.model_ = LogisticRegression()
        else:
            self.model_ = LinearRegression()

        (
            self.X_train_,
            self.X_test_,
            self.y_train_,
            self.y_test_,
        ) = self._train_test_split(self.X, self.y, self.random_state, self.test_size)

    def _train_test_split(
        self, X: pd.DataFrame, y: pd.DataFrame, random_state: int, test_size: float
    ) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
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
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        X_train = X_train.to_numpy()
        X_test = X_test.to_numpy()
        y_train = y_train.to_numpy()
        y_test = y_test.to_numpy()

        if X_train.ndim == 1:
            X_train = X_train.reshape(-1, 1)

        if X_test.ndim == 1:
            X_test = X_test.reshape(-1, 1)

        return X_train, X_test, y_train, y_test

    def set_X_cols(self, cols: list[str]) -> None:
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
        self.model_ = self.model_.fit(self.X_train(), self.y_train_)

    def predict_test(self) -> np.ndarray:
        """Returns the models predictions on the testing input"""
        return self.model_.predict(self.X_test())

    def score_test(self) -> np.ndarray:
        """Returns the accuracy score for the fitted model"""
        return self.model_.score(self.X_test(), self.y_test_)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Returns the models predictions for a given input set

        Args:
            X - Input data, must dim-2 must match dim-2 of the training set

        Returns:
            The models predicted outut
        """
        return self.model_.predict(X)


class CorrelationAnalysis:
    """Helper class for correlation analysis."""

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

    def corr_coef(self, a: str, b: str) -> float:
        """
        Provides the correlation coefficient between two variables in the dataset

        Args:
            a - One variable to be compared
            b - The other variable
        """
        return self.data[a].corr(self.data[b])


def plot_linear_fit(X, y_pred, y_test):
    """
    Makes a scatter plot of fit between predicted and actual y.

    Args:
        X: Vector of X inputs
        y_pred: Vector of y predictions
        y_test: Vector of y actual

    Returns: None
    """
    plt.scatter(X, y_test, color="black")
    plt.scatter(X, y_pred, color="blue", marker=".")
    plt.show()
