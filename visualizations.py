"""This module holds functions for visualizations"""

import pandas as pd

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
