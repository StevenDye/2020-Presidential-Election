"""This module holds functions for visualizations"""

import pandas as pd

def display_results(actual, prediction, counties):
    """This function returns the number of votes each county received and the number
    of votes they were projected to get"""
    
    final_results = pd.DataFrame(prediction).set_index(actual.index)
    final_results = pd.merge(actual, final_results, left_index=True, right_index=True)
    final_results = pd.merge(counties, final_results, left_index=True, right_index=True)
    final_results = final_results.rename(columns={0: "Predictions"})
    final_results['Percent off'] = final_results.apply(lambda row: (row.iloc[2]-row.iloc[1])/row.iloc[1]*100, axis=1)
    final_results['Percent off Abs'] = final_results['Percent off'].abs() 
    
    print(final_results['Donald Trump'].sum(), final_results['Predictions'].sum(), final_results['Percent off Abs'].sum()/len(actual))
    
    return final_results


