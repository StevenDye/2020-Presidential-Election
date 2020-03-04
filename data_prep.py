"""This module prepares the data for analysis"""
import pandas as pd
from data_dicts import (EDU_2012, EDU_2016, EDU_2018,
                        AGE_SEX_2012, AGE_SEX_2016, AGE_SEX_2018,
                        RACE_2012, RACE_2016, RACE_2018,
                        INCOME_2012, INCOME_2016, INCOME_2018) 


def county_info_2012():
    """This function reads in the county csv data files and prepares them for analysis"""

    # read in csvs
    state_area = pd.read_csv('data/state_area.csv')
    df_edu = pd.read_csv('data/2012/2012-Edu/ACSST5Y2012.S1501_data_with_overlays_2020-01-21T124942.csv',
                         header=1, low_memory=False)
    df_age_sex = pd.read_csv('data/2012/2012-Age/ACSST5Y2012.S0101_data_with_overlays_2020-01-21T124608.csv',
                             header=1, low_memory=False)
    df_race = pd.read_csv('data/2012/2012-Race/ACSDP5Y2012.DP05_data_with_overlays_2020-01-21T125225.csv',
                          header=1, low_memory=False)
    df_income = pd.read_csv('data/2012/2012-Income/ACSST5Y2012.S1901_data_with_overlays_2020-01-21T124756.csv',
                            header=1, low_memory=False)

    # select specific columns
    edu = df_edu[['Geographic Area Name'] + EDU_2012]
    age_sex = df_age_sex[['Geographic Area Name'] + AGE_SEX_2012]
    race = df_race[['Geographic Area Name'] + RACE_2012]
    income = df_income[['Geographic Area Name'] + INCOME_2012] 

    # merge dataframes
    df = pd.merge(edu, age_sex, on='Geographic Area Name')
    df = pd.merge(df, race, on='Geographic Area Name')
    df = pd.merge(df, income, on='Geographic Area Name')
    
    _ = fix_counties(df['Geographic Area Name'])
    
    df = _.merge(df, on='Geographic Area Name')
    df = df.drop(columns = ['Geographic Area Name'])
    df = df.merge(state_area, on='County')

    # rename features
    df = df.rename(columns={"Total!!Estimate!!Total population":
                            "Total population",
                            "Total!!Estimate!!SUMMARY INDICATORS!!Median age (years)":
                            "Median age",
                            "Total!!Estimate!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)":
                            "Sex ratio (males per 100 females)",
                            "Male!!Estimate!!SUMMARY INDICATORS!!Median age (years)":
                            "Male Median age",
                            "Female!!Estimate!!SUMMARY INDICATORS!!Median age (years)":
                            "Female Median age",
                            "Estimate!!RACE!!White":
                            "Total White",
                            "Estimate!!RACE!!Black or African American":
                            "Total Black or African American",
                            "Estimate!!RACE!!American Indian and Alaska Native":
                            "Total American Indian and Alaska Native",
                            "Estimate!!RACE!!Asian":
                            "Total Asian",
                            "Estimate!!HISPANIC OR LATINO AND RACE!!Hispanic or Latino (of any race)":
                            "Total Hispanic or Latino",
                            "Households!!Estimate!!Mean income (dollars)":
                            "Households Mean income",
                            "Households!!Estimate!!Median income (dollars)":
                            "Households Median income",
                            "Total!!Estimate!!Less than 9th grade":
                            "Percent Less than 9th grade",
                            "Total!!Estimate!!9th to 12th grade, no diploma":
                            "Percent 9th to 12th grade, no diploma",
                            "Total!!Estimate!!High school graduate (includes equivalency)":
                            "Percent High school graduate",
                            "Total!!Estimate!!Some college, no degree":
                            "Percent Some college, no degree",
                            "Total!!Estimate!!Associate's degree":
                            "Percent Associate's degree",
                            "Total!!Estimate!!Bachelor's degree":
                            "Percent Bachelor's degree",
                            "Total!!Estimate!!Graduate or professional degree":
                            "Percent Graduate or professional degree",
                            "Percent!!RACE!!White":
                            "Percent White",
                            "Percent!!RACE!!Black or African American":
                            "Percent Black or African American",
                            "Percent!!RACE!!American Indian and Alaska Native":
                            "Percent American Indian and Alaska Native",
                            "Percent!!RACE!!Asian":
                            "Percent Asian",
                            "Percent!!HISPANIC OR LATINO AND RACE!!Hispanic or Latino (of any race)":
                            "Percent Hispanic or Latino"})

    # Calculate counts for education
    df['Total Less than 9th grade'] = df["Percent Less than 9th grade"] * df["Total population"] / 100
    df['Total 9th to 12th grade, no diploma'] = df["Percent 9th to 12th grade, no diploma"] * df["Total population"] / 100
    df['Total High school graduate'] = df["Percent High school graduate"] * df["Total population"] / 100
    df['Total Some college, no degree'] = df["Percent Some college, no degree"] * df["Total population"] / 100
    df["Total Associate's degree"] = (df["Percent Associate's degree"] * df["Total population"] / 100)
    df["Total Bachelor's degree"] = (df["Percent Bachelor's degree"] * df["Total population"] / 100)
    df["Total Graduate or professional degree"] = (df["Percent Graduate or professional degree"] * df["Total population"] / 100)

    # Calculate population density
    df["Population Density"] = (df["Total population"] / df['Size'])
    
    # Add year to county info
    df['County'] = df['County'] + ', 2012' 

    return df


def county_info_2016():
    """This function reads in the county csv data files and prepares them for analysis"""

    # read in csvs
    state_area = pd.read_csv('data/state_area.csv')
    df_edu = pd.read_csv('data/2016/2016-Edu/ACSST5Y2016.S1501_data_with_overlays_2020-01-19T112805.csv',
                         header=1, low_memory=False)
    df_age_sex = pd.read_csv('data/2016/2016-Age/ACSST5Y2016.S0101_data_with_overlays_2020-01-19T114609.csv',
                             header=1, low_memory=False)
    df_race = pd.read_csv('data/2016/2016-Race/ACSDP5Y2016.DP05_data_with_overlays_2020-01-19T114033.csv',
                          header=1, low_memory=False)
    df_income = pd.read_csv('data/2016/2016-Income-2/ACSST5Y2016.S1901_data_with_overlays_2020-01-19T114923.csv',
                            header=1, low_memory=False)

    # select specific columns
    edu = df_edu[['Geographic Area Name'] + EDU_2016]
    age_sex = df_age_sex[['Geographic Area Name'] + AGE_SEX_2016]
    race = df_race[['Geographic Area Name'] + RACE_2016]
    income = df_income[['Geographic Area Name'] + INCOME_2016] 
    
    # merge dataframes
    df = pd.merge(edu, age_sex, on='Geographic Area Name')
    df = pd.merge(df, race, on='Geographic Area Name')
    df = pd.merge(df, income, on='Geographic Area Name')
    
    _ = fix_counties(df['Geographic Area Name'])
    
    df = _.merge(df, on='Geographic Area Name')
    df = df.drop(columns = ['Geographic Area Name'])
    df = df.merge(state_area, on='County')

    # rename features
    df = df.rename(columns={"Total!!Estimate!!Population 25 years and over!!Less than 9th grade":
                            "Total Less than 9th grade",
                            "Total!!Estimate!!Population 25 years and over!!9th to 12th grade, no diploma":
                            "Total 9th to 12th grade, no diploma",
                            "Total!!Estimate!!Population 25 years and over!!High school graduate (includes equivalency)":
                            "Total High school graduate",
                            "Total!!Estimate!!Population 25 years and over!!Some college, no degree":
                            "Total Some college, no degree",
                            "Total!!Estimate!!Population 25 years and over!!Associate's degree":
                            "Total Associate's degree",
                            "Total!!Estimate!!Population 25 years and over!!Bachelor's degree":
                            "Total Bachelor's degree",
                            "Total!!Estimate!!Population 25 years and over!!Graduate or professional degree":
                            "Total Graduate or professional degree",
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
                            "Households!!Estimate!!Mean income (dollars)":
                            "Households Mean income",
                            "Households!!Estimate!!Median income (dollars)":
                            "Households Median income",
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
                            "Estimate!!RACE!!One race!!White":
                            "Total White",
                            "Estimate!!RACE!!One race!!Black or African American":
                            "Total Black or African American",
                            "Estimate!!RACE!!One race!!American Indian and Alaska Native":
                            "Total American Indian and Alaska Native",
                            "Estimate!!RACE!!One race!!Asian":
                            "Total Asian",
                            "Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)":
                            "Total Hispanic or Latino",
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
                            "Percent Graduate or professional degree"})

    # Calculate population density
    df["Population Density"] = (df["Total population"] / df['Size'])
    
    # Add year to county info
    df['County'] = df['County'] + ', 2016' 

    return df


def county_info_2018():
    """This function reads in the county csv data files for 2018 and prepares them for analysis"""

    # read in csvs
    state_area = pd.read_csv('data/state_area.csv')
    df_edu = pd.read_csv('data/2018/2018-Edu/ACSST5Y2018.S1501_data_with_overlays_2020-01-19T112805.csv',
                         header=1, low_memory=False)
    df_age_sex = pd.read_csv('data/2018/2018-Age/ACSST5Y2018.S0101_data_with_overlays_2020-01-19T114609.csv',
                             header=1, low_memory=False)
    df_race = pd.read_csv('data/2018/2018-Race/ACSDP5Y2018.DP05_data_with_overlays_2020-01-19T114033.csv',
                          header=1, low_memory=False)
    df_income = pd.read_csv('data/2018/2018-Income-2/ACSST5Y2018.S1901_data_with_overlays_2020-01-19T114923.csv',
                            header=1, low_memory=False)

    # select specific columns
    edu = df_edu[['Geographic Area Name'] + EDU_2018]
    age_sex = df_age_sex[['Geographic Area Name'] + AGE_SEX_2018]
    race = df_race[['Geographic Area Name'] + RACE_2018]
    income = df_income[['Geographic Area Name'] + INCOME_2018] 
    
    # merge dataframes
    df = pd.merge(edu, age_sex, on='Geographic Area Name')
    df = pd.merge(df, race, on='Geographic Area Name')
    df = pd.merge(df, income, on='Geographic Area Name')
    
    _ = fix_counties(df['Geographic Area Name'])
    
    df = _.merge(df, on='Geographic Area Name')
    df = df.drop(columns = ['Geographic Area Name'])
    df = df.merge(state_area, on='County')

    # rename features
    df = df.rename(columns={"Geographic Area Name": "County",
                            "Estimate!!Total!!Population 25 years and over!!Less than 9th grade":
                            "Total Less than 9th grade",
                            "Estimate!!Total!!Population 25 years and over!!9th to 12th grade, no diploma":
                            "Total 9th to 12th grade, no diploma",
                            "Estimate!!Total!!Population 25 years and over!!High school graduate (includes equivalency)":
                            "Total High school graduate",
                            "Estimate!!Total!!Population 25 years and over!!Some college, no degree":
                            "Total Some college, no degree",
                            "Estimate!!Total!!Population 25 years and over!!Associate's degree":
                            "Total Associate's degree",
                            "Estimate!!Total!!Population 25 years and over!!Bachelor's degree":
                            "Total Bachelor's degree",
                            "Estimate!!Total!!Population 25 years and over!!Graduate or professional degree":
                            "Total Graduate or professional degree",
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
                            "Percent Estimate!!RACE!!Total population!!One race!!White":
                            "Percent White",
                            "Percent Estimate!!RACE!!Total population!!One race!!Black or African American":
                            "Percent Black or African American",
                            "Percent Estimate!!RACE!!Total population!!One race!!American Indian and Alaska Native":
                            "Percent American Indian and Alaska Native",
                            "Percent Estimate!!RACE!!Total population!!One race!!Asian":
                            "Percent Asian",
                            "Percent Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)":
                            "Percent Hispanic or Latino",
                            "Estimate!!Households!!Mean income (dollars)":
                            "Households Mean income",
                            "Estimate!!Households!!Median income (dollars)":
                            "Households Median income",
                            "Estimate!!RACE!!Total population!!One race!!White":
                            "Total White",
                            "Estimate!!RACE!!Total population!!One race!!Black or African American":
                            "Total Black or African American",
                            "Estimate!!RACE!!Total population!!One race!!American Indian and Alaska Native":
                            "Total American Indian and Alaska Native",
                            "Estimate!!RACE!!Total population!!One race!!Asian":
                            "Total Asian",
                            "Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)":
                            "Total Hispanic or Latino"})

    # calculate population density
    df["Population Density"] = (df["Total population"] / df['Size'])

    return df


def results_info(year):
    """This function prepares election results for analysis"""
    df_results = pd.read_csv('data/countypres_2000-2016.csv')

    # delete duplicates
    del_index = [39827, 39828, 39829, 39854, 39855, 39856, 39860, 39861,
                 39862, 39914, 39915, 39916, 39917, 39918, 39919, 49178,
                 49179, 49180, 49205, 49206, 49207, 49211, 49212, 49213,
                 49265, 49266, 49267, 49268, 49269, 49270]

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
                                  'Hillary Clinton': 'Democrat',
                                  'Other': 'Third'})

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
                                  'Barack Obama': 'Democrat',
                                  'Other': 'Third'})
        
    return res


def county_split(column):
    """This function splits the county column into county and state,
    and then recombines them to county"""
    _ = column.str.split(',', expand=True)
    _ = _.rename(columns={0: 'Cnt', 1: 'State'})
    _['Cnt'] = _['Cnt'].apply(lambda x: x.strip())
    _['State'] = _['State'].apply(lambda x: x.strip())
    column = pd.merge(column, _, left_index=True, right_index=True)

    return column


def create_targets(df):
    """This function creates the percent targets for our model"""
    df['Percent Republican'] = (df['Republican'] / df['Total population']).astype(float)
    df['Percent Democrat'] = (df['Democrat'] / df['Total population']).astype(float)
    df['Percent Third'] = (df['Third'] / df['Total population']).astype(float)

    return df


def fix_counties(column):
    """This function splits the county column into county and state, and then recombines them to county"""
    _ = column.str.split(',', expand=True)
    _ = _.rename(columns={0: 'County', 1: 'State'})
    _['County'] = _['County'].apply(lambda x: x.strip())
    _['State'] = _['State'].apply(lambda x: x.strip())
    df = pd.merge(column, _, left_index=True, right_index=True)

    # Add the word County to the end of District of Columbia so we can merge with results
    df['County'][df['State'].str.contains('District of Columbia') == True] = df['County'][df['State'].str.contains('District of Columbia') == True].apply(lambda x: x + ' County')

    # Strip the word Parish at the end of Louisiana parishes so we can merge with results
    df['County'][df['State'].str.contains('Louisiana') == True] = df['County'][df['State'].str.contains('Louisiana') == True].apply(lambda x: x[:-7])

    # Add the word County to the end of Louisiana so we can merge with results
    df['County'][df['State'].str.contains('Louisiana') == True] = df['County'][df['State'].str.contains('Louisiana') == True].apply(lambda x: x + ' County')
    
    df['County'] = df['County'] + ', ' + df['State']
    
    return df


