"""This module prepares models and performs analysis"""

import numpy as np
from sklearn import metrics

def run_model(model, X_train, X_test, y_train, y_test):
    """This function calculates the root mean square of the train and test data for the inserted model"""
    print('Training R^2 :', model.score(X_train, y_train))
    y_pred_train = model.predict(X_train)
    print('Training Root Mean Square Error', np.sqrt(metrics.mean_squared_error(y_train, y_pred_train)))
    print('\n----------------\n')
    print('Testing R^2 :', model.score(X_test, y_test))
    y_pred_test = model.predict(X_test)
    print('Testing Root Mean Square Error', np.sqrt(metrics.mean_squared_error(y_test, y_pred_test)))