"""This module prepares the data for analysis"""
import pandas as pd
from data_dicts import (edu_2012_count, edu_2016_count, edu_2018_count,
                        age_sex_2012, age_sex_2016, age_sex_2018,
                        race_2012_count, race_2016_per, race_2018_per,
                        income_2012, income_2016, income_2018)


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
    county = df_edu['Geographic Area Name']
    edu = df_edu[edu_2012_count]
    age_sex = df_age_sex[age_sex_2012]
    race = df_race[race_2012_count]
    income = df_income[income_2012]

    county = county_prep(county, state_area, '2012')
    
    
    #county = county_split(county)
    #county = clean_states(county)
    #county['Cnt'] = county['Cnt'] + ', ' + county['State']
    #county = county.merge(state_area, left_on='Cnt', right_on='County')
    #county = county.drop(columns=['Geographic Area Name', 'Cnt'])
    #county['County'] = county['County'] + ', 2012'

    # merge dataframes
    df = pd.merge(county, edu, left_index=True, right_index=True)
    df = pd.merge(df, age_sex, left_index=True, right_index=True)
    df = pd.merge(df, race, left_index=True, right_index=True)
    df = pd.merge(df, income, left_index=True, right_index=True)

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
                            "Estimate!!HISPANIC OR LATINO AND RACE!!Total population":
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
                            "Percent Graduate or professional degree"})
    
    df['Total Less than 9th grade'] = df["Percent Less than 9th grade"] * df["Total population"] / 100
    df['Total 9th to 12th grade, no diploma'] = df["Percent 9th to 12th grade, no diploma"] * df["Total population"] / 100
    df['Total High school graduate'] = df["Percent High school graduate"] * df["Total population"] / 100
    df['Total Some college, no degree'] = df["Percent Some college, no degree"] * df["Total population"] / 100
    df["Total Associate's degree"] = (df["Percent Associate's degree"] * df["Total population"] / 100)
    df["Total Bachelor's degree"] = (df["Percent Bachelor's degree"] * df["Total population"] / 100)
    df["Total Graduate or professional degree"] = (df["Percent Graduate or professional degree"] * df["Total population"] / 100)
    df["Population Density"] = (df["Total population"] / df['Size'])

    # Drop incorrect DC value
    df = df.drop([156])

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
    county = df_edu['Geographic Area Name']
    edu = df_edu[edu_2016_count]
    age_sex = df_age_sex[age_sex_2016]
    race = df_race[race_2016_per]
    income = df_income[income_2016]

    county = county_prep(county, state_area, '2016')
    
    #county = county_split(county)
    #county = clean_states(county)
    #county['Cnt'] = county['Cnt'] + ', ' + county['State']
    #county = county.merge(state_area, left_on='Cnt', right_on='County')
    #county = county.drop(columns=['Geographic Area Name', 'Cnt'])
    #county['County'] = county['County'] + ', 2016'

    # merge dataframes
    df = pd.merge(county, edu, left_index=True, right_index=True)
    df = pd.merge(df, age_sex, left_index=True, right_index=True)
    df = pd.merge(df, race, left_index=True, right_index=True)
    df = pd.merge(df, income, left_index=True, right_index=True)

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
                           "Percent Hispanic or Latino"})
    
    df['Total White'] = df["Percent White"] * df["Total population"] / 100
    df['Total Black or African American'] = (df["Percent Black or African American"] * df["Total population"] / 100)
    df['Total American Indian and Alaska Native'] = (df["Percent American Indian and Alaska Native"] * df["Total population"] / 100)
    df['Total Asian'] = df["Percent Asian"] * df["Total population"] / 100
    df['Total Hispanic or Latino'] = (df["Percent Hispanic or Latino"] * df["Total population"] / 100)
    df["Population Density"] = (df["Total population"] / df['Size'])

    # Drop incorrect DC value
    df = df.drop([381])

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
    county = df_edu['Geographic Area Name']
    edu = df_edu[edu_2018_count]
    age_sex = df_age_sex[age_sex_2018]
    race = df_race[race_2018_per]
    income = df_income[income_2018]

    # merge dataframes
    df = pd.merge(county, edu, left_index=True, right_index=True)
    df = pd.merge(df, age_sex, left_index=True, right_index=True)
    df = pd.merge(df, race, left_index=True, right_index=True)
    df = pd.merge(df, income, left_index=True, right_index=True)

    df['Total White'] = (df['Percent Estimate!!RACE!!Total population!!One race!!White'] * df["Estimate!!Total!!Total population"] / 100)
    df['Total Black or African American'] = (df['Percent Estimate!!RACE!!Total population!!One race!!Black or African American'] * df["Estimate!!Total!!Total population"] / 100)
    df['Total American Indian and Alaska Native'] = (df['Percent Estimate!!RACE!!Total population!!One race!!American Indian and Alaska Native'] * df["Estimate!!Total!!Total population"] / 100)
    df['Total Asian'] = (df['Percent Estimate!!RACE!!Total population!!One race!!Asian'] * df["Estimate!!Total!!Total population"] / 100)
    df['Total Hispanic or Latino'] = (df['Percent Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)'] * df["Estimate!!Total!!Total population"] / 100)
    df["Population Density"] = (df["Estimate!!Total!!Total population"] / df['Size'])

    # rename features
    df = df.rename(columns={"Geographic Area Name": "County",
                            "Estimate!!Total!!Population 25 years and over!!Less than 9th grade":
                            "Percent Less than 9th grade",
                            "Estimate!!Total!!Population 25 years and over!!9th to 12th grade, no diploma":
                            "Percent 9th to 12th grade, no diploma",
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
                            "Total Estimate!!RACE!!Total population!!One race!!White":
                            "Total White",
                            "Total Estimate!!RACE!!Total population!!One race!!Black or African American":
                            "Total Black or African American",
                            "Total Estimate!!RACE!!Total population!!One race!!American Indian and Alaska Native":
                            "Total American Indian and Alaska Native",
                            "Total Estimate!!RACE!!Total population!!One race!!Asian":
                            "Total Asian",
                            "Total Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)":
                            "Total Hispanic or Latino",
                            "Estimate!!Households!!Mean income (dollars)":
                            "Households Mean income",
                            "Estimate!!Households!!Median income (dollars)":
                            "Households Median income"})
    
    df = df.drop(columns=race_2018_per)
    # Drop incorrect DC value
    df = df.drop([319])
    
    return df


def results_info(year):
    """This function prepares the 2016 election results for analysis"""
    df_results = pd.read_csv('data/countypres_2000-2016.csv')

    # delete duplicates
    del_index = [39827, 39828, 39829, 39854, 39855, 39856, 39860, 39861,
                 39862, 39914, 39915, 39916, 39917, 39918, 39919, 49178,
                 49179, 49180, 49205, 49206, 49207, 49211, 49212, 49213,
                 49265, 49266, 49267, 49268, 49269, 49270]

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
    df['Percent Republican'] = (df['Republican']/df['Total population']).astype(float)
    df['Percent Democrat'] = (df['Democrat']/df['Total population']).astype(float)
    df['Percent Other'] = (df['Other']/df['Total population']).astype(float)

    return df

    
def county_prep(df, states_info, year):
    """This function splits the county column into county and state, and then recombines them to county"""
    _ = df.str.split(',', expand=True)
    _ = _.rename(columns={0: 'Cnt', 1: 'State'})
    _['Cnt'] = _['Cnt'].apply(lambda x: x.strip())
    _['State'] = _['State'].apply(lambda x: x.strip())
    df = pd.merge(df, _, left_index=True, right_index=True)
    
    # Add the word County to the end of Washington city so we can merge with results
    df['Cnt'][df['State'].str.contains('District of Columbia') == True] = df['Cnt'][df['State'].str.contains('District of Columbia') == True].apply(lambda x: x + ' County')

    # Strip the word Parish at the end of Louisiana parishes so we can merge with results
    df['Cnt'][df['State'].str.contains('Louisiana') == True] = df['Cnt'][df['State'].str.contains('Louisiana') == True].apply(lambda x: x[:-7])

    # Add the word County to the end of Louisiana so we can merge with results
    df['Cnt'][df['State'].str.contains('Louisiana') == True] = df['Cnt'][df['State'].str.contains('Louisiana') == True].apply(lambda x: x + ' County')
    
    df['Cnt'] = df['Cnt'] + ', ' + df['State']
    df = df.merge(states_info, left_on='Cnt', right_on='County')
    df = df.drop(columns=['Geographic Area Name', 'Cnt'])
    df['County'] = df['County'] + ', ' + year
    
    return df
    