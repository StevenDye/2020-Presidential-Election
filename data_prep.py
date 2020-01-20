"""This module prepares the data for analysis"""
import pandas as pd
from data_dicts import (edu_cols_2016, edu_cols_2018,
                        age_sex_cols_2016, age_sex_cols_2018,
                        race_cols_2016, race_cols_2018,
                        income_cols_2016, income_cols_2018)


def county_info_2016():
    """This function reads in the county csv data files and prepares them for analysis"""

    # read in csvs
    df_edu = pd.read_csv('data/2016/2016-Edu/ACSST5Y2016.S1501_data_with_overlays_2020-01-19T112805.csv',
                         header=1, low_memory=False)
    df_age_sex = pd.read_csv('data/2016/2016-Age/ACSST5Y2016.S0101_data_with_overlays_2020-01-19T114609.csv',
                             header=1, low_memory=False)
    df_race = pd.read_csv('data/2016/2016-Race/ACSDP5Y2016.DP05_data_with_overlays_2020-01-19T114033.csv',
                          header=1, low_memory=False)
    df_income = pd.read_csv('data/2016/2016-Income-2/ACSST5Y2016.S1901_data_with_overlays_2020-01-19T114923.csv',
                            header=1, low_memory=False)
    
    
    # df_edu = pd.read_csv('data/2016/ACSST5Y2016-Edu/ACSST5Y2016.S1501_data_with_overlays_2020-01-15T123834.csv',
    #                      header=1, low_memory=False)
    # df_age_sex = pd.read_csv('data/2016/ACSST5Y2016-Sex/ACSST5Y2016.S0101_data_with_overlays_2020-01-15T131242.csv',
    #                          header=1, low_memory=False)
    # df_race = pd.read_csv('data/2016/ACSDP5Y2016-Race/ACSDP5Y2016.DP05_data_with_overlays_2020-01-15T133652.csv',
    #                       header=1, low_memory=False)
    # df_income = pd.read_csv('data/2016/2016-Income/ACSST5Y2016.S1901_data_with_overlays_2020-01-16T145642.csv',
    #                         header=1, low_memory=False)

    # select specific columns
    county = df_edu['Geographic Area Name']
    edu = df_edu[edu_cols_2016]
    age_sex = df_age_sex[age_sex_cols_2016]
    race = df_race[race_cols_2016]
    income = df_income[income_cols_2016]
    
    _ = county.str.split(',', expand=True)
    _ = _.rename(columns={0: 'Cnt', 1: 'State'})
    _['Cnt'] = _['Cnt'].apply(lambda x: x.strip())
    _['State'] = _['State'].apply(lambda x: x.strip())
    county = pd.merge(county, _, left_index=True, right_index=True)
    
    # Add the word County to the end of Washington city so we can merge with results
    county['Cnt'][county['State'].str.contains('District of Columbia') == True] = county['Cnt'][county['State'].str.contains('District of Columbia') == True].apply(lambda x: x + ' County')
    
    # Strip the word Parish at the end of Louisiana parishes so we can merge with results
    county['Cnt'][county['State'].str.contains('Louisiana') == True] = county['Cnt'][county['State'].str.contains('Louisiana') == True].apply(lambda x: x[:-7])
    
    # Add the word County to the end of Louisiana parishes so we can merge with results
    county['Cnt'][county['State'].str.contains('Louisiana') == True] = county['Cnt'][county['State'].str.contains('Louisiana') == True].apply(lambda x: x + ' County')
    
    county['Cnt'] = county['Cnt'] + ', ' + county['State'] + ', 2016'
    county = county.drop(columns=['Geographic Area Name', 'State'])
    
    # merge dataframes
    df = pd.merge(county, edu, left_index=True, right_index=True)
    df = pd.merge(df, age_sex, left_index=True, right_index=True)
    df = pd.merge(df, race, left_index=True, right_index=True)
    df = pd.merge(df, income, left_index=True, right_index=True)
    

    # rename features
    df = df.rename(columns={"Cnt": "County",
                            "Percent!!Estimate!!Population 25 years and over!!Less than 9th grade":
                            "Percent Less than 9th grade",
                            "Percent!!Estimate!!Population 25 years and over!!9th to 12th grade, no diploma":
                            "Percent 9th to 12th grade, no diploma",
                            "Percent!!Estimate!!Population 25 years and over!!High school graduate (includes equivalency)":
                            "Percent High school graduate",
                            "Percent!!Estimate!!Population 25 years and over!!Some college, no degree":
                            "Percent Some college, no degree",
                            "Percent!!Estimate!!Population 25 years and over!!Associate's degree":
                            "Percent Associate's degree",
                            "Percent!!Estimate!!Population 25 years and over!!Bachelor's degree":
                            "Percent Bachelor's degree",
                            "Percent!!Estimate!!Population 25 years and over!!Graduate or professional degree":
                            "Percent Graduate or professional degree",
                            "Total!!Estimate!!Total population":
                            "Total population",
                            "Total!!Estimate!!SUMMARY INDICATORS!!Median age (years)":
                            "Median age",
                            "Total!!Estimate!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)":
                            "Sex ratio (males per 100 females)",
                            "Male!!Estimate!!SUMMARY INDICATORS!!Median age (years)":
                            "Male Median age",
                            "Female!!Estimate!!SUMMARY INDICATORS!!Median age (years)":
                            "Female Median age",
                            "Percent!!RACE!!One race!!White":
                            "Percent White",
                            "Percent!!RACE!!One race!!Black or African American":
                            "Percent Black or African American",
                            "Percent!!RACE!!One race!!American Indian and Alaska Native":
                            "Percent American Indian and Alaska Native",
                            "Percent!!RACE!!One race!!Asian":
                            "Percent Asian",
                            "Percent!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)":
                            "Percent Hispanic or Latino",
                            "Households!!Estimate!!Mean income (dollars)":
                            "Households Mean income",
                            "Households!!Estimate!!Median income (dollars)":
                            "Households Median income"})

    return df


def county_info_2018():
    """This function reads in the county csv data files for 2018 and prepares them for analysis"""

    # read in csvs
    df_edu = pd.read_csv('data/2018/2018-Edu/ACSST5Y2018.S1501_data_with_overlays_2020-01-19T112805.csv',
                         header=1, low_memory=False)
    df_age_sex = pd.read_csv('data/2018/2018-Age/ACSST5Y2018.S0101_data_with_overlays_2020-01-19T114609.csv',
                             header=1, low_memory=False)
    df_race = pd.read_csv('data/2018/2018-Race/ACSDP5Y2018.DP05_data_with_overlays_2020-01-19T114033.csv',
                          header=1, low_memory=False)
    df_income = pd.read_csv('data/2018/2018-Income-2/ACSST5Y2018.S1901_data_with_overlays_2020-01-19T114923.csv',
                            header=1, low_memory=False)
    
    # df_edu = pd.read_csv('data/2018/ACSST5Y2018-Edu/ACSST5Y2018.S1501_data_with_overlays_2020-01-16T122405.csv',
    #                      header=1, low_memory=False)
    # df_age_sex = pd.read_csv('data/2018/ACSST5Y2018-Sex/ACSST5Y2018.S0101_data_with_overlays_2020-01-16T114607.csv',
    #                          header=1, low_memory=False)
    # df_race = pd.read_csv('data/2018/ACSDP5Y2018-Race/ACSDP5Y2018.DP05_data_with_overlays_2020-01-16T115900.csv',
    #                       header=1, low_memory=False)
    # df_income = pd.read_csv('data/2018/2018-Income/ACSST5Y2018.S1901_data_with_overlays_2020-01-16T145642.csv',
    #                         header=1, low_memory=False)

    # select specific columns
    county = df_edu['Geographic Area Name']
    edu = df_edu[edu_cols_2018]
    age_sex = df_age_sex[age_sex_cols_2018]
    race = df_race[race_cols_2018]
    income = df_income[income_cols_2018]

    # merge dataframes
    df = pd.merge(county, edu, left_index=True, right_index=True)
    df = pd.merge(df, age_sex, left_index=True, right_index=True)
    df = pd.merge(df, race, left_index=True, right_index=True)
    df = pd.merge(df, income, left_index=True, right_index=True)

    # rename features
    df = df.rename(columns={"Geographic Area Name": "County",
                            "Estimate!!Percent!!Population 25 years and over!!Less than 9th grade":
                            "Percent Less than 9th grade",
                            "Estimate!!Percent!!Population 25 years and over!!9th to 12th grade, no diploma":
                            "Percent 9th to 12th grade, no diploma",
                            "Estimate!!Percent!!Population 25 years and over!!High school graduate (includes equivalency)":
                            "Percent High school graduate",
                            "Estimate!!Percent!!Population 25 years and over!!Some college, no degree":
                            "Percent Some college, no degree",
                            "Estimate!!Percent!!Population 25 years and over!!Associate's degree":
                            "Percent Associate's degree",
                            "Estimate!!Percent!!Population 25 years and over!!Bachelor's degree":
                            "Percent Bachelor's degree",
                            "Estimate!!Percent!!Population 25 years and over!!Graduate or professional degree":
                            "Percent Graduate or professional degree",
                            "Estimate!!Total!!Total population":
                            "Total population",
                            "Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Median age (years)":
                            "Median age",
                            "Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)":
                            "Sex ratio (males per 100 females)",
                            "Estimate!!Male!!Total population!!SUMMARY INDICATORS!!Median age (years)":
                            "Male Median age",
                            "Estimate!!Female!!Total population!!SUMMARY INDICATORS!!Median age (years)":
                            "Female Median age",
                            "Percent Estimate!!RACE!!Total population!!One race!!White": "Percent White",
                            "Percent Estimate!!RACE!!Total population!!One race!!Black or African American":
                            "Percent Black or African American",
                            "Percent Estimate!!RACE!!Total population!!One race!!American Indian and Alaska Native":
                            "Percent American Indian and Alaska Native",
                            "Percent Estimate!!RACE!!Total population!!One race!!Asian": "Percent Asian",
                            "Percent Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)":
                            "Percent Hispanic or Latino",
                            "Estimate!!Households!!Mean income (dollars)":
                            "Households Mean income",
                            "Estimate!!Households!!Median income (dollars)":
                            "Households Median income"})
    return df


def results_info(year):
    """This function prepares the 2016 election results for analysis"""
    df_results = pd.read_csv('data/countypres_2000-2016.csv')

    # delete duplicates
    del_index = [49178, 49179, 49180, 49205, 49206, 49207, 49211, 49212,
                 49213, 49265, 49266, 49267, 49268, 49269, 49270]
    
    df_results.loc[df_results['county'] == 'District of Columbia', 'county'] = 'Washington city'
    df_results = df_results.drop(del_index)

    df_results['County'] = df_results['county'] + ' County, ' + df_results['state'] + ', ' + str(year)
    df = df_results[df_results.year == year]
    df = df.pivot(index='County', columns='candidate',
                            values=['state', 'candidatevotes']).reset_index()

    if year == 2016:
        res = pd.merge(df['County'], pd.DataFrame(df['state']['Donald Trump']),
                       left_index=True, right_index=True)
        res = pd.merge(res, pd.DataFrame(df['candidatevotes']['Donald Trump']),
                       left_index=True, right_index=True)
        res = pd.merge(res, pd.DataFrame(df['candidatevotes']['Hillary Clinton']),
                       left_index=True, right_index=True)
        res = pd.merge(res, pd.DataFrame(df['candidatevotes']['Other']),
                       left_index=True, right_index=True)
        res = res.rename(columns={'Donald Trump_x': 'State',
                                  'Donald Trump_y': 'Republican',
                                  'Hillary Clinton': 'Democrat'})
        
    if year == 2012:
        res = pd.merge(df['County'], pd.DataFrame(df['state']['Mitt Romney']),
                       left_index=True, right_index=True)
        res = pd.merge(res, pd.DataFrame(df['candidatevotes']['Mitt Romney']),
                       left_index=True, right_index=True)
        res = pd.merge(res, pd.DataFrame(df['candidatevotes']['Barack Obama']),
                       left_index=True, right_index=True)
        res = pd.merge(res, pd.DataFrame(df['candidatevotes']['Other']),
                       left_index=True, right_index=True)
        res = res.rename(columns={'Mitt Romney_x': 'State',
                                  'Mitt Romney_y': 'Republican',
                                  'Barack Obama': 'Democrat'})

    return res


def create_targets(df):
    """This function creates the percent targets for our model"""
    df['Percent Republican'] = (df['Republican']/df['Total population']).astype(float)
    df['Percent Democrat'] = (df['Democrat']/df['Total population']).astype(float)
    df['Percent Other'] = (df['Other']/df['Total population']).astype(float)
    
    return df