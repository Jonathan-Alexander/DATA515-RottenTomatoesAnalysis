'''
regression_analysis.py
'''

import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

class RegressionAnalysis:
    def __init__(self, X, y, is_categorical, random_state = 123, test_size=0.25):
        self.X = X
        self.y = y
        self.is_categorical = is_categorical
        self.random_state = random_state
        self.test_size = test_size
        self.col_indexes = None
        
        if is_categorical:
            self.model_ = LogisticRegression()
        else:
            self.model_ = LinearRegression()
        
        self.X_train_, self.X_test_, self.y_train_, self.y_test_ = self._train_test_split(self.X, self.y, self.random_state, self.test_size)
        
    def _train_test_split(self, X, y, random_state, test_size):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        X_train = X_train.to_numpy()
        X_test = X_test.to_numpy()
        y_train = y_train.to_numpy()
        y_test = y_test.to_numpy()

        if X_train.ndim == 1:
            X_train = X_train.reshape(-1, 1)

        if X_test.ndim == 1:
            X_test = X_test.reshape(-1, 1)

        return X_train, X_test, y_train, y_test
    
    def set_X_cols(self, cols):
        '''
        set a subset of columns to be used as input
        '''
        self.col_indexes = [self.X.columns.get_loc(c) for c in cols]
        return
    
    def X_train(self):
        return self.X_train_[:, self.col_indexes]
    
    def X_test(self):
        return self.X_test_[:, self.col_indexes]

    def fit_train(self):
        '''
        Fits the model (Linear or Logistic)
        using the supplied columns, or all the columns in X if not given
        
        @param id_cols - list of columns in X to use when fitting
        @return void
        '''
        self.model_ = self.model_.fit(self.X_train(), self.y_train_)
        return
    
    def predict_test(self):
        return self.model_.predict(self.X_test())
    
    def score_test(self):
        return self.model_.score(self.X_test(), self.y_test_)
    
    def predict(self, X):
        return self.model.predict(X)
    

        