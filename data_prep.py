"""This module prepares the data for analysis"""
import pandas as pd
from data_dicts import education_columns, age_sex_columns, race_columns, income_columns

def county_info():
    """This function reads in the county csv data files and prepares them for analysis"""
    
    # read in csvs
    df_edu = pd.read_csv('data/2016/ACSST5Y2016-Edu/ACSST5Y2016.S1501_data_with_overlays_2020-01-15T123834.csv', header=1, low_memory=False)
    df_age_sex = pd.read_csv('data/2016/ACSST5Y2016-Sex/ACSST5Y2016.S0101_data_with_overlays_2020-01-15T131242.csv', header=1, low_memory=False)
    df_race = pd.read_csv('data/2016/ACSDP5Y2016-Race/ACSDP5Y2016.DP05_data_with_overlays_2020-01-15T133652.csv', header=1, low_memory=False)
    df_income = pd.read_csv('data/2016/ACSST5Y2016-Income/ACSST5Y2016.S1901_data_with_overlays_2020-01-15T140106.csv', header=1, low_memory=False)
    
    # select specific columns
    county = df_edu['Geographic Area Name']
    edu = df_edu[education_columns]
    age_sex = df_age_sex[age_sex_columns]
    race = df_race[race_columns]
    income = df_income[income_columns]
    
    # merge dataframes
    df = pd.merge(county, edu, left_index=True, right_index=True)
    df = pd.merge(df, age_sex, left_index=True, right_index=True)
    df = pd.merge(df, race, left_index=True, right_index=True)
    df = pd.merge(df, income, left_index=True, right_index=True)
    
    # rename features
    df = df.rename(columns={"Geographic Area Name": "County",
                   "Percent!!Estimate!!Percent high school graduate or higher": "Percent high school graduate or higher",
                   "Percent!!Estimate!!Percent bachelor's degree or higher": "Percent bachelor's degree or higher",
                   "Percent Males!!Estimate!!Percent high school graduate or higher": "Males Percent high school graduate or higher",
                   "Percent Males!!Estimate!!Percent bachelor's degree or higher": "Males Percent bachelor's degree or higher",
                   "Percent Females!!Estimate!!Percent high school graduate or higher": "Females Percent high school graduate or higher",
                   "Percent Females!!Estimate!!Percent bachelor's degree or higher": "Females Percent bachelor's degree or higher",
                   "Total!!Estimate!!SUMMARY INDICATORS!!Median age (years)": "Median age",
                   "Total!!Estimate!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)": "Sex ratio (males per 100 females)",
                   "Male!!Estimate!!SUMMARY INDICATORS!!Median age (years)": "Male Median age",
                   "Female!!Estimate!!SUMMARY INDICATORS!!Median age (years)": "Female Median age",
                   "Percent!!RACE!!One race!!White": "Percent White",
                   "Percent!!RACE!!One race!!Black or African American": "Percent Black or African American",
                   "Percent!!RACE!!One race!!American Indian and Alaska Native": "Percent American Indian and Alaska Native",
                   "Percent!!RACE!!One race!!Asian": "Percent Asian",
                   "Percent!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)": "Percent Hispanic or Latino",
                   "Households!!Estimate!!Median income (dollars)": "Households Median income",
                   "Households!!Estimate!!Mean income (dollars)": "Households Mean income"})
    
    return df



def results_info():
    """This function prepares the 2016 election results for analysis"""
    df_results = pd.read_csv('data/countypres_2000-2016.csv')
    
    # delete duplicates
    del_index = [49178, 49179, 49180, 49205, 49206, 49207, 49211, 49212, 49213, 49265, 49266, 49267, 49268, 49269, 49270]
    df_results = df_results.drop(del_index)
    
    df_results['County'] = df_results['county'] + ' County, ' + df_results['state']   
    df_2016 = df_results[df_results.year == 2016]
    df_2016 = df_2016.pivot(index='County', columns='candidate', values=['state', 'candidatevotes']).reset_index()

    result = pd.merge(df_2016['County'], pd.DataFrame(df_2016['state']['Donald Trump']), left_index=True, right_index=True)
    result = pd.merge(result, pd.DataFrame(df_2016['candidatevotes']['Donald Trump']), left_index=True, right_index=True)
    result = pd.merge(result, pd.DataFrame(df_2016['candidatevotes']['Hillary Clinton']), left_index=True, right_index=True)
    result = pd.merge(result, pd.DataFrame(df_2016['candidatevotes']['Other']), left_index=True, right_index=True)
    result = result.rename(columns={'Donald Trump_x': 'State', 'Donald Trump_y': 'Donald Trump'})

    return result

# MIT Election Data and Science Lab, 2018, "County Presidential Election Returns 2000-2016", https://doi.org/10.7910/DVN/VOQCHQ, Harvard Dataverse, V6, UNF:6:ZZe1xuZ5H2l4NUiSRcRf8Q== [fileUNF]