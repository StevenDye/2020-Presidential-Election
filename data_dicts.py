"""This module is a repository of lists and dictionaries that will be used in the analysis"""


"""Education"""
# 2012 Education columns
# These are actually percentages, there are no actual counts in 2012
EDU_2012 = ["Total!!Estimate!!Less than 9th grade",
            "Total!!Estimate!!9th to 12th grade, no diploma",
            "Total!!Estimate!!High school graduate (includes equivalency)",
            "Total!!Estimate!!Some college, no degree",
            "Total!!Estimate!!Associate's degree",
            "Total!!Estimate!!Bachelor's degree",
            "Total!!Estimate!!Graduate or professional degree"]


# 2016 Education count columns
EDU_2016_COUNT = ["Total!!Estimate!!Population 25 years and over!!Less than 9th grade",
                  "Total!!Estimate!!Population 25 years and over!!9th to 12th grade, no diploma",
                  "Total!!Estimate!!Population 25 years and over!!High school graduate (includes equivalency)",
                  "Total!!Estimate!!Population 25 years and over!!Some college, no degree",
                  "Total!!Estimate!!Population 25 years and over!!Associate's degree",
                  "Total!!Estimate!!Population 25 years and over!!Bachelor's degree",
                  "Total!!Estimate!!Population 25 years and over!!Graduate or professional degree"]

# 2016 Education percentages columns
EDU_2016_PER = ["Percent!!Estimate!!Population 25 years and over!!Less than 9th grade",
                "Percent!!Estimate!!Population 25 years and over!!9th to 12th grade, no diploma",
                "Percent!!Estimate!!Population 25 years and over!!High school graduate (includes equivalency)",
                "Percent!!Estimate!!Population 25 years and over!!Some college, no degree",
                "Percent!!Estimate!!Population 25 years and over!!Associate's degree",
                "Percent!!Estimate!!Population 25 years and over!!Bachelor's degree",
                "Percent!!Estimate!!Population 25 years and over!!Graduate or professional degree"]

# 2018 Eduction count columns
EDU_2018_COUNT = ["Estimate!!Total!!Population 25 years and over!!Less than 9th grade",
                  "Estimate!!Total!!Population 25 years and over!!9th to 12th grade, no diploma",
                  "Estimate!!Total!!Population 25 years and over!!High school graduate (includes equivalency)",
                  "Estimate!!Total!!Population 25 years and over!!Some college, no degree",
                  "Estimate!!Total!!Population 25 years and over!!Associate's degree",
                  "Estimate!!Total!!Population 25 years and over!!Bachelor's degree",
                  "Estimate!!Total!!Population 25 years and over!!Graduate or professional degree"]

# 2018 Eduction percentages columns
EDU_2018_PER = ["Estimate!!Percent!!Population 25 years and over!!Less than 9th grade",
                "Estimate!!Percent!!Population 25 years and over!!9th to 12th grade, no diploma",
                "Estimate!!Percent!!Population 25 years and over!!High school graduate (includes equivalency)",
                "Estimate!!Percent!!Population 25 years and over!!Some college, no degree",
                "Estimate!!Percent!!Population 25 years and over!!Associate's degree",
                "Estimate!!Percent!!Population 25 years and over!!Bachelor's degree",
                "Estimate!!Percent!!Population 25 years and over!!Graduate or professional degree"]

EDU_2016 = EDU_2016_COUNT + EDU_2016_PER
EDU_2018 = EDU_2018_COUNT + EDU_2018_PER


"""Age and Sex"""
# 2012 Age and Sex columns
AGE_SEX_2012 = ['Total!!Estimate!!Total population',
                'Total!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                'Total!!Estimate!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)',
                'Male!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                'Female!!Estimate!!SUMMARY INDICATORS!!Median age (years)']

# 2016 Age and Sex columns
AGE_SEX_2016 = ['Total!!Estimate!!Total population',
                'Total!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                'Total!!Estimate!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)',
                'Male!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                'Female!!Estimate!!SUMMARY INDICATORS!!Median age (years)']

# 2018 Age and Sex columns
AGE_SEX_2018 = ['Estimate!!Total!!Total population',
                'Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Median age (years)',
                'Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)',
                'Estimate!!Male!!Total population!!SUMMARY INDICATORS!!Median age (years)',
                'Estimate!!Female!!Total population!!SUMMARY INDICATORS!!Median age (years)']


"""Race"""
# 2012 Race count columns
RACE_2012_COUNT = ['Estimate!!RACE!!White',
                   'Estimate!!RACE!!Black or African American',
                   'Estimate!!RACE!!American Indian and Alaska Native',
                   'Estimate!!RACE!!Asian',
                   'Estimate!!HISPANIC OR LATINO AND RACE!!Total population']

# 2012 Race percent columns
RACE_2012_PER = ['Percent!!RACE!!White',
                 'Percent!!RACE!!Black or African American',
                 'Percent!!RACE!!American Indian and Alaska Native',
                 'Percent!!RACE!!Asian',
                 'Percent!!HISPANIC OR LATINO AND RACE!!Total population']

# 2016 Race count columns
RACE_2016_COUNT = ['Estimate!!RACE!!One race!!White',
                   'Estimate!!RACE!!One race!!Black or African American',
                   'Estimate!!RACE!!One race!!American Indian and Alaska Native',
                   'Estimate!!RACE!!One race!!Asian',
                   'Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)']

# 2016 Race percent columns
RACE_2016_PER = ['Percent!!RACE!!One race!!White',
                 'Percent!!RACE!!One race!!Black or African American',
                 'Percent!!RACE!!One race!!American Indian and Alaska Native',
                 'Percent!!RACE!!One race!!Asian',
                 'Percent!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)']


# 2018 Race features count
RACE_2018_COUNT = ['Estimate!!RACE!!Total population!!One race!!White',
                   'Estimate!!RACE!!Total population!!One race!!Black or African American',
                   'Estimate!!RACE!!Total population!!One race!!American Indian and Alaska Native',
                   'Estimate!!RACE!!Total population!!One race!!Asian',
                   'Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)']

# 2018 Race features percent
RACE_2018_PER = ['Percent Estimate!!RACE!!Total population!!One race!!White',
                 'Percent Estimate!!RACE!!Total population!!One race!!Black or African American',
                 'Percent Estimate!!RACE!!Total population!!One race!!American Indian and Alaska Native',
                 'Percent Estimate!!RACE!!Total population!!One race!!Asian',
                 'Percent Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)']

RACE_2012 = RACE_2012_COUNT + RACE_2012_PER
RACE_2016 = RACE_2016_COUNT + RACE_2016_PER
RACE_2018 = RACE_2018_COUNT + RACE_2018_PER


"""Income Features"""
# 2012 Income features
INCOME_2012 = ['Households!!Estimate!!Median income (dollars)',
               'Households!!Estimate!!Mean income (dollars)']

# 2016 Income features
INCOME_2016 = ['Households!!Estimate!!Median income (dollars)',
               'Households!!Estimate!!Mean income (dollars)']

# 2018 Income features
INCOME_2018 = ['Estimate!!Households!!Median income (dollars)',
               'Estimate!!Households!!Mean income (dollars)']



"""Features"""

PERCENT_FEATURES = ['Percent Less than 9th grade',
                    'Percent 9th to 12th grade, no diploma',
                    'Percent High school graduate',
                    'Percent Some college, no degree',
                    "Percent Associate's degree",
                    "Percent Bachelor's degree",
                    'Percent Graduate or professional degree',
                    'Median age',
                    'Sex ratio (males per 100 females)',
                    'Male Median age',
                    'Female Median age',
                    'Percent White',
                    'Percent Black or African American',
                    'Percent American Indian and Alaska Native',
                    'Percent Asian',
                    'Percent Hispanic or Latino',
                    'Households Median income',
                    'Households Mean income',
                    'Population Density']

COUNT_FEATURES = ['Median age',
                  'Sex ratio (males per 100 females)',
                  'Male Median age',
                  'Female Median age',
                  'Total White',
                  'Total Black or African American',
                  'Total American Indian and Alaska Native',
                  'Total Asian',
                  'Total Hispanic or Latino',
                  'Households Median income',
                  'Households Mean income',
                  'Total Less than 9th grade',
                  'Total 9th to 12th grade, no diploma',
                  'Total High school graduate',
                  'Total Some college, no degree',
                  "Total Associate's degree",
                  "Total Bachelor's degree",
                  'Total Graduate or professional degree',
                  'Population Density']


"""Miscellaneous"""
# Columns dropped from original dataframe
DROP_COLS = ['County', 'State', 'Republican', 'Democrat', 'Other', 'Total population',
             'Percent Republican', 'Percent Democrat', 'Percent Other']

# Alaska is removed from this list
STATES_LIST = ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado',
               'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
               'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
               'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
               'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
               'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
               'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
               'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
               'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

ELECTORAL_DICT = {'Alabama': 9,
                  'Alaska': 3,
                  'Arizona': 11,
                  'Arkansas': 6,
                  'California': 55,
                  'Colorado': 9,
                  'Connecticut': 7,
                  'Delaware': 3,
                  'District of Columbia': 3,
                  'Florida': 29,
                  'Georgia': 16,
                  'Hawaii': 4,
                  'Idaho': 4,
                  'Illinois': 20,
                  'Indiana': 11,
                  'Iowa': 6,
                  'Kansas': 6,
                  'Kentucky': 8,
                  'Louisiana': 8,
                  'Maine': 4,
                  'Maryland': 10,
                  'Massachusetts': 11,
                  'Michigan': 16,
                  'Minnesota': 10,
                  'Mississippi': 6,
                  'Missouri': 10,
                  'Montana': 3,
                  'Nebraska': 5,
                  'Nevada': 6,
                  'New Hampshire': 4,
                  'New Jersey': 14,
                  'New Mexico': 5,
                  'New York': 29,
                  'North Carolina': 15,
                  'North Dakota': 3,
                  'Ohio': 18,
                  'Oklahoma': 7,
                  'Oregon': 7,
                  'Pennsylvania': 20,
                  'Rhode Island': 4,
                  'South Carolina': 9,
                  'South Dakota': 3,
                  'Tennessee': 11,
                  'Texas': 38,
                  'Utah': 6,
                  'Vermont': 3,
                  'Virginia': 13,
                  'Washington': 12,
                  'West Virginia': 5,
                  'Wisconsin': 10,
                  'Wyoming': 3}
