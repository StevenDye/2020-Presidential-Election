"""This module prepares models and performs analysis"""

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler



def make_predictions(party, model, X, y, df):
    """This function predicts the percent of votes that a party will get in a county, calculates
    the total number of votes obtained, and the percent off"""
    
    y_hat = model.predict(X)
    res = pd.DataFrame(df['County']).merge(df['Total population'],
                                           left_index=True,
                                           right_index=True)
    res = res.merge(y, left_index=True, right_index=True)
    res = res.merge(df[party], left_index=True, right_index=True)
    res = res.merge(pd.DataFrame(y_hat), left_index=True, right_index=True)
    res = res.rename(columns={0: f'{party} Predictions'})
    
    #res[f'{party} % off'] = ((df[party]-res[f'{party} Predictions']) / df[party])*100
    #res[f'{party} % off'] = ((res[f'{party} Predictions'] - y) / y)*100
    #res[f'{party} % off Abs'] = res[f'{party} % off'].abs()
    #res[f'{party} Votes Prediction'] = (res[f'{party} Predictions']* res['Total population']).round()
    
    return res


def run_model(model, X_train, X_test, y_train, y_test):
    """This function calculates the root mean square of the train and test data for the inserted model"""
    print('Training R^2 :', model.score(X_train, y_train))
    y_pred_train = model.predict(X_train)
    print('Training Root Mean Square Error', np.sqrt(mse(y_train, y_pred_train)))
    print('----------------')
    print('Testing R^2 :', model.score(X_test, y_test))
    y_pred_test = model.predict(X_test)
    print('Testing Root Mean Square Error', np.sqrt(mse(y_test, y_pred_test)))
    
    
def lin_mod_func(X_train, X_test, y_train, y_test):
    "This function takes in training and testing data, runs the function run_model, and returns a linear fitted model"
    scaler = StandardScaler()
    scaler.fit(X_train)
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    run_model(linreg, X_train, X_test, y_train, y_test)
    
    return linreg.fit(X_train, y_train)


def combine_predictions(pred_R, pred_D, pred_O, df):
    """This function combines the prediction results for each party"""
    df = pd.merge(df['State'], pred_R, left_index=True, right_index=True)
    df = df.merge(pred_D, left_index=True, right_index=True)
    df = df.merge(pred_O, left_index=True, right_index=True)
    df = df.drop(columns=['Total population', 'Total population_y',
                                  'County_y', 'County'])
    df = df.rename(columns={'Total population_x': 'Total population',
                                    'County_x': 'County'})
    
    return df