import unittest
import os
import json
import pandas as pd
import numpy as np
from unittest import mock
from sklearn.linear_model import LinearRegression, LogisticRegression

from rotten_tomatoes.utils.regression import RegressionAnalysis, CorrelationAnalysis
from rotten_tomatoes.utils import regression as regression

class TestRegressionAnalysis(unittest.TestCase):
    """
    Class used to test the rotten_tomatoes.utils.regression RegressionAnalysis
    """

    def test_regressionanalysis_create_linear(self):
        """One shot test for LinearRegression"""
        x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y = [0, 0, 0]

        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        is_categorical = False

        reg = RegressionAnalysis(x_df, y_df, is_categorical)

        self.assertTrue(reg != None)
        self.assertIsInstance(reg.model_, LinearRegression)

    def test_regressionanalysis_create_logistic(self):
        """One shot test for Logistic Regression"""

        x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y = [0, 0, 0]

        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        is_categorical = True

        reg = RegressionAnalysis(x_df, y_df, is_categorical)

        self.assertTrue(reg != None)
        self.assertTrue(reg.model_, LogisticRegression)

    def test_regressionanalysis_splitsize(self):
        """Test the split size argument is correclty handled""" 
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
        """Edge case, test correct handling of 1-dimensional data, improper handling causes error when fitting"""
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
        """Tests using a subset of input data for fitting"""
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
        """Edge case fitting using 1 dim input"""
        x = {"a": [0, 0]}
        y = [0, 0]
        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        reg = RegressionAnalysis(x_df.a, y_df, False, test_size = 0.5)
        reg.fit_train()

        self.assertEqual(reg.X_train_.ndim, 2)
        self.assertEqual(reg.X_test_.ndim, 2)
        self.assertIsNotNone(reg.model_.coef_)

    def test_regressionanalysis_fit(self):
        """One shot test of fitting"""
        x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y = [0, 0, 0]
        x_df = pd.DataFrame(x)
        y_df = pd.DataFrame(y)
        is_categorical = False

        reg = RegressionAnalysis(x_df, y_df, is_categorical)
        reg.fit_train()
        self.assertIsNotNone(reg.model_.coef_)

    def test_regressionanalysis_oneshot(self):
        """Tests that fitting and prediction are accurate"""
        x = pd.DataFrame([1, 2, 3, 4, 5])
        y = pd.DataFrame([2, 3, 4, 5, 6])
        reg = RegressionAnalysis(x, y, False)

        reg.fit_train()

        y_pred = reg.predict_test()
        self.assertTrue(np.array_equal(y_pred, [[3], [5]]))

    def test_regressionanalysis_predict(self):
        """Tests general prediction case using data not in train or test"""
        x = pd.DataFrame([1, 2, 3, 4, 5])
        y = pd.DataFrame([2, 3, 4, 5, 6])
        reg = RegressionAnalysis(x, y, False)

        reg.fit_train()

        y_pred = reg.predict([[10], [11], [12]])
        self.assertTrue(np.array_equal(np.rint(y_pred), [[11], [12], [13]]))

    def test_regressionanalysis_notest(self):
        """Tests using 0 test_size in RegressionAnalysis"""
        x = pd.DataFrame([1, 2, 3, 4, 5])
        y = pd.DataFrame([2, 3, 4, 5, 6])
        reg = RegressionAnalysis(x, y, False, test_size = 0)

        self.assertTrue(np.array_equal(reg.X_train_, reg.X_test_))
        self.assertTrue(np.array_equal(reg.y_train_, reg.y_test_))

    def test_regressionanalysis_scoretest(self):
        """Tests scoring agains the test set"""
        x = pd.DataFrame([1, 2, 3, 4, 5])
        y = pd.DataFrame([2, 3, 4, 5, 6])
        reg = RegressionAnalysis(x, y, False, test_size = 0)
        reg.fit_train()

        self.assertEqual(reg.score_test(), 1)

class TestCorrelationAnalysis(unittest.TestCase):
    """
    Class to test the rotten_tomatoes.utils.regression.py CorrelationAnalysis class
    """
        
    def test_correlationanalysis_oneshot(self):
        """One shot test of CorrelationAnalysis"""
        d = pd.DataFrame({'a':[1, 2, 3, 4, 5], 'b': [5, 4, 3, 2, 1]})
        corr = CorrelationAnalysis(d)
        self.assertIsInstance(corr, CorrelationAnalysis)
        self.assertAlmostEqual(corr.corr_coef('a', 'b'), -1)

    def test_correlationanalysis_matrix(self):
        """Checks for correctness of correlation matrix"""
        d = pd.DataFrame({'a':[1, 2, 3, 4, 5], 'b': [5, 4, 3, 2, 1]})
        corr = CorrelationAnalysis(d)
        self.assertIsInstance(corr, CorrelationAnalysis)
        self.assertTrue(np.array_equal(corr.corr_matrix(), [[1, -1], [-1, 1]]))

    def test_correlationanalysis_subsetmatrix(self):
        """Tests correlation matrix with a subset of cols"""
        d = pd.DataFrame({'a':[1, 2, 3, 4, 5], 'b': [5, 4, 3, 2, 1], 'c': [1, 2, 3, 4, 5]})
        corr = CorrelationAnalysis(d)
        self.assertIsInstance(corr, CorrelationAnalysis)
        self.assertTrue(np.array_equal(corr.corr_matrix(subset=['a', 'b']), [[1, -1], [-1, 1]]))

class TestRegression(unittest.TestCase):
    """
    Class to test the general methods of RegressionAnalysis
    """

    @mock.patch("%s.regression.plt" % __name__)
    def test_regression_plotlinfit(self, mock_plt):
       x = [0, 1]
       y_pred = [1, 2]
       y = [1, 2]

       regression.plot_linear_fit(x, y_pred, y)
       self.assertTrue(mock_plt.show.called)
       regression.plot_linear_fit(x, y_pred, y, x_label = "TEST", y_label = "TEST", title="TEST")
       self.assertTrue(mock_plt.show.called)


