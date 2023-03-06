import unittest
import os
import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression

from rotten_tomatoes.utils.regression import RegressionAnalysis, CorrelationAnalysis

class TestRegressionAnalysis(unittest.TestCase):
    """
    Class used to test the rotten_tomatoes.utils.regression RegressionAnalysis

    """
    def test_regressionanalysis_create_linear(self):
        x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y = [0, 0, 0]

        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        is_categorical = False

        reg = RegressionAnalysis(x_df, y_df, is_categorical)

        self.assertTrue(reg != None)
        self.assertIsInstance(reg.model_, LinearRegression)

    def test_regressionanalysis_create_logistic(self):

        x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y = [0, 0, 0]

        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        is_categorical = True

        reg = RegressionAnalysis(x_df, y_df, is_categorical)

        self.assertTrue(reg != None)
        self.assertTrue(reg.model_, LogisticRegression)

    def test_regressionanalysis_splitsize(self):
        x = [[1, 2, 3], [4, 5, 6]]
        y = [0, 0]
        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        reg = RegressionAnalysis(x_df, y_df, False, test_size = 0.5)

        self.assertEqual(reg.X_train_.shape, (1, 3))
        self.assertEqual(reg.X_test_.shape, (1, 3))
        self.assertEqual(reg.y_train_.shape, (1, 1))
        self.assertEqual(reg.y_test_.shape, (1, 1))

    def test_regressionanalysis_onedim(self):
        x = [[1], [2], [3], [4], [5], [6]]
        y = [0, 0, 0, 0, 0 , 0]
        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        reg = RegressionAnalysis(x_df, y_df, False)

        self.assertEqual(reg.X_train_.shape, (4, 1))
        self.assertEqual(reg.X_test_.shape, (2, 1))
        self.assertEqual(reg.y_train_.shape, (4, 1))
        self.assertEqual(reg.y_test_.shape, (2, 1))

    def test_regressionanalysis_setcols(self):
        x = {"a": [0, 0],"b": [0, 0],"c": [0, 0]}
        y = [0, 0]
        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        reg = RegressionAnalysis(x_df, y_df, False, test_size = 0.5)

        self.assertTrue(np.array_equal(reg.X_train(), [[0, 0, 0]]))
        self.assertTrue(np.array_equal(reg.X_test(), [[0, 0, 0]]))

        reg.set_X_cols(["a", "b"])
        
        self.assertTrue(np.array_equal(reg.X_train(), [[0, 0]]))
        self.assertTrue(np.array_equal(reg.X_test(), [[0, 0]]))

    def test_regressionanalysis_onecol(self):
        x = {"a": [0, 0]}
        y = [0, 0]
        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        reg = RegressionAnalysis(x_df, y_df, False, test_size = 0.5)
        reg.fit_train()

        self.assertIsNotNone(reg.model_.coef_)

    def test_regressionanalysis_fit(self):
        x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y = [0, 0, 0]
        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        is_categorical = False

        reg = RegressionAnalysis(x_df, y_df, is_categorical)
        reg.fit_train()
        self.assertIsNotNone(reg.model_.coef_)

    def test_regressionanalysis_oneshot(self):
        x = pd.DataFrame([1, 2, 3, 4, 5])
        y = pd.DataFrame([2, 3, 4, 5, 6])
        reg = RegressionAnalysis(x, y, False)

        reg.fit_train()

        y_pred = reg.predict_test()
        self.assertTrue(np.array_equal(y_pred, [[3], [5]]))

    def test_regressionanalysis_predict(self):
        x = pd.DataFrame([1, 2, 3, 4, 5])
        y = pd.DataFrame([2, 3, 4, 5, 6])
        reg = RegressionAnalysis(x, y, False)

        reg.fit_train()

        y_pred = reg.predict([[10], [11], [12]])
        self.assertTrue(np.array_equal(np.rint(y_pred), [[11], [12], [13]]))

class TestCorrelationAnalysis(unittest.TestCase):
    """
    Class to test the rotten_tomatoes.utils.regression.py CorrelationAnalysis class
    """
        
    def test_correlationanalysis_oneshot(self):
        d = pd.DataFrame({'a':[1, 2, 3, 4, 5], 'b': [5, 4, 3, 2, 1]})
        corr = CorrelationAnalysis(d)
        self.assertIsInstance(corr, CorrelationAnalysis)
        self.assertAlmostEqual(corr.corr_coef('a', 'b'), -1)

    def test_correlationanalysis_matrix(self):
        d = pd.DataFrame({'a':[1, 2, 3, 4, 5], 'b': [5, 4, 3, 2, 1]})
        corr = CorrelationAnalysis(d)
        self.assertIsInstance(corr, CorrelationAnalysis)
        self.assertTrue(np.array_equal(corr.corr_matrix(), [[1, -1], [-1, 1]]))


