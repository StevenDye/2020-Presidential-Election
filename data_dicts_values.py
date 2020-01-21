"""This module is a repository of lists and dictionaries that will be used in the analysis"""

# Education features for 2012
edu_cols_2012 = ["Total!!Estimate!!Less than 9th grade",
                 "Total!!Estimate!!9th to 12th grade, no diploma",
                 "Total!!Estimate!!High school graduate (includes equivalency)",
                 "Total!!Estimate!!Some college, no degree",
                 "Total!!Estimate!!Associate's degree",
                 "Total!!Estimate!!Bachelor's degree",
                 "Total!!Estimate!!Graduate or professional degree"]

# Education features for 2016
edu_cols_2016 = ["Total!!Estimate!!Population 25 years and over!!Less than 9th grade",
                 "Total!!Estimate!!Population 25 years and over!!9th to 12th grade, no diploma",
                 "Total!!Estimate!!Population 25 years and over!!High school graduate (includes equivalency)",
                 "Total!!Estimate!!Population 25 years and over!!Some college, no degree",
                 "Total!!Estimate!!Population 25 years and over!!Associate's degree",
                 "Total!!Estimate!!Population 25 years and over!!Bachelor's degree",
                 "Total!!Estimate!!Population 25 years and over!!Graduate or professional degree"]

# Eduction featues for 2018
edu_cols_2018 = ["Estimate!!Total!!Population 25 years and over!!Less than 9th grade",
                 "Estimate!!Total!!Population 25 years and over!!9th to 12th grade, no diploma",
                 "Estimate!!Total!!Population 25 years and over!!High school graduate (includes equivalency)",
                 "Estimate!!Total!!Population 25 years and over!!Some college, no degree",
                 "Estimate!!Total!!Population 25 years and over!!Associate's degree",
                 "Estimate!!Total!!Population 25 years and over!!Bachelor's degree",
                 "Estimate!!Total!!Population 25 years and over!!Graduate or professional degree"]


# 2012 Age and Sex features
age_sex_cols_2012 = ['Total!!Estimate!!Total population',
                     'Total!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                     'Total!!Estimate!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)',
                     'Male!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                     'Female!!Estimate!!SUMMARY INDICATORS!!Median age (years)']

# 2016 Age and Sex features
age_sex_cols_2016 = ['Total!!Estimate!!Total population',
                     'Total!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                     'Total!!Estimate!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)',
                     'Male!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                     'Female!!Estimate!!SUMMARY INDICATORS!!Median age (years)']

# 2018 Age and Sex features
age_sex_cols_2018 = ['Estimate!!Total!!Total population',
                     'Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Median age (years)',
                     'Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)',
                     'Estimate!!Male!!Total population!!SUMMARY INDICATORS!!Median age (years)',
                     'Estimate!!Female!!Total population!!SUMMARY INDICATORS!!Median age (years)']


# 2012 Race features
race_cols_2012 = ['Estimate!!RACE!!White',
                  'Estimate!!RACE!!Black or African American',
                  'Estimate!!RACE!!American Indian and Alaska Native',
                  'Estimate!!RACE!!Asian',
                  'Estimate!!HISPANIC OR LATINO AND RACE!!Total population']

# 2016 Race features
race_cols_2016 = ['Percent!!RACE!!One race!!White',
                  'Percent!!RACE!!One race!!Black or African American',
                  'Percent!!RACE!!One race!!American Indian and Alaska Native',
                  'Percent!!RACE!!One race!!Asian',
                  'Percent!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)']

# 2018 Race features
race_cols_2018 = ['Percent Estimate!!RACE!!Total population!!One race!!White',
                  'Percent Estimate!!RACE!!Total population!!One race!!Black or African American',
                  'Percent Estimate!!RACE!!Total population!!One race!!American Indian and Alaska Native',
                  'Percent Estimate!!RACE!!Total population!!One race!!Asian',
                  'Percent Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)']


# 2012 Income features
income_cols_2012 = ['Households!!Estimate!!Median income (dollars)',
                    'Households!!Estimate!!Mean income (dollars)']

# 2016 Income features
income_cols_2016 = ['Households!!Estimate!!Median income (dollars)',
                    'Households!!Estimate!!Mean income (dollars)']

# 2018 Income features
income_cols_2018 = ['Estimate!!Households!!Median income (dollars)',
                    'Estimate!!Households!!Mean income (dollars)']


# Columns dropped from original dataframe
drop_cols = ['County', 'State', 'Republican', 'Democrat', 'Other', 'Total population']
