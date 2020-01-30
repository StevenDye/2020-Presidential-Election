"""This module holds functions for visualizations"""

import pandas as pd
from data_dicts import PERCENT_FEATURES, COUNT_FEATURES, STATES_LIST

# This function is currently not in use
def display_results(actual, prediction, counties):
    """This function returns the number of votes each county received and the
    number of votes they were projected to get"""

    res = pd.DataFrame(prediction).set_index(actual.index)
    res = pd.merge(actual, res, left_index=True, right_index=True)
    res = pd.merge(counties, res, left_index=True, right_index=True)
    res = res.rename(columns={0: "Predictions"})
    #res['Percent off'] = res.apply(lambda row: (row.iloc[2]-row.iloc[1])/row.iloc[1]*100, axis=1)
    res['Percent off'] = ((res['Percent Republican']-res['Predictions']) / res['Predictions'])*100
    res['Percent off Abs'] = res['Percent off'].abs()
    res['R Votes Prediction'] = res['Predictions']* res['Total population']

    print(res['Percent Republican'].sum(),
          res['Predictions'].sum(),
          res['Percent off Abs'].sum()/len(actual))

    return res


def state_results_check(df):
    """This function validates combined state results"""
    interests = ['Republican','Republican Predictions',
                 'Democrat', 'Democrat Predictions',
                 'Third','Third Predictions']
    state_results = pd.DataFrame(STATES_LIST)
    results = pd.DataFrame()
    state_results = state_results.rename(columns={0: 'State'})
    for state in STATES_LIST:
        results = results.append(df[df.State == state][interests].sum(), ignore_index=True)

    state_results = state_results.merge(results, left_index=True, right_index=True)
    state_results['Winner'] = state_results['Democrat Predictions'] - state_results['Republican Predictions']
    state_results['Winner'] = state_results['Winner'].astype(int)
    state_results['Democrat'] = state_results['Democrat'].astype(int)
    state_results['Democrat Predictions'] = state_results['Democrat Predictions'].astype(int)
    state_results['Third'] = state_results['Third'].astype(int)
    state_results['Third Predictions'] = state_results['Third Predictions'].astype(int)
    state_results['Republican'] = state_results['Republican'].astype(int)
    state_results['Republican Predictions'] = state_results['Republican Predictions'].astype(int)
    
    return state_results


def state_results_predict(df):
    """This function combines prediction results by state"""
    interests2 = ['Republican Predictions', 'Democrat Predictions', 'Third Predictions']
    state_results = pd.DataFrame(STATES_LIST)
    results = pd.DataFrame()
    state_results = state_results.rename(columns={0: 'State'})
    for state in STATES_LIST:
        results = results.append(df[df.State == state][interests2].sum(), ignore_index=True)

    state_results = state_results.merge(results, left_index=True, right_index=True)
    state_results['Winner'] = state_results['Democrat Predictions'] - state_results['Republican Predictions']
    state_results['Winner'] = state_results['Winner'].astype(int)
    #state_results['Democrat'] = state_results['Democrat'].astype(int)
    state_results['Democrat Predictions'] = state_results['Democrat Predictions'].astype(int)
    #state_results['Third'] = state_results['Third'].astype(int)
    state_results['Third Predictions'] = state_results['Third Predictions'].astype(int)
    #state_results['Republican'] = state_results['Republican'].astype(int)
    state_results['Republican Predictions'] = state_results['Republican Predictions'].astype(int)
    
    return state_results