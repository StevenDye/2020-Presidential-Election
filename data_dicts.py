"""This module is a repository of lists and dictionaries that will be used in the analysis"""


"""Education"""

# Education count for 2012
edu_2012_count = ["Total!!Estimate!!Less than 9th grade",
                  "Total!!Estimate!!9th to 12th grade, no diploma",
                  "Total!!Estimate!!High school graduate (includes equivalency)",
                  "Total!!Estimate!!Some college, no degree",
                  "Total!!Estimate!!Associate's degree",
                  "Total!!Estimate!!Bachelor's degree",
                  "Total!!Estimate!!Graduate or professional degree"]


# Education count for 2016
edu_2016_count = ["Total!!Estimate!!Population 25 years and over!!Less than 9th grade",
                  "Total!!Estimate!!Population 25 years and over!!9th to 12th grade, no diploma",
                  "Total!!Estimate!!Population 25 years and over!!High school graduate (includes equivalency)",
                  "Total!!Estimate!!Population 25 years and over!!Some college, no degree",
                  "Total!!Estimate!!Population 25 years and over!!Associate's degree",
                  "Total!!Estimate!!Population 25 years and over!!Bachelor's degree",
                  "Total!!Estimate!!Population 25 years and over!!Graduate or professional degree"]

# Education percentages for 2016
edu_2016_per = ["Percent!!Estimate!!Population 25 years and over!!Less than 9th grade",
                "Percent!!Estimate!!Population 25 years and over!!9th to 12th grade, no diploma",
                "Percent!!Estimate!!Population 25 years and over!!High school graduate (includes equivalency)",
                "Percent!!Estimate!!Population 25 years and over!!Some college, no degree",
                "Percent!!Estimate!!Population 25 years and over!!Associate's degree",
                "Percent!!Estimate!!Population 25 years and over!!Bachelor's degree",
                "Percent!!Estimate!!Population 25 years and over!!Graduate or professional degree"]


# Eduction count for 2018
edu_2018_count = ["Estimate!!Total!!Population 25 years and over!!Less than 9th grade",
                  "Estimate!!Total!!Population 25 years and over!!9th to 12th grade, no diploma",
                  "Estimate!!Total!!Population 25 years and over!!High school graduate (includes equivalency)",
                  "Estimate!!Total!!Population 25 years and over!!Some college, no degree",
                  "Estimate!!Total!!Population 25 years and over!!Associate's degree",
                  "Estimate!!Total!!Population 25 years and over!!Bachelor's degree",
                  "Estimate!!Total!!Population 25 years and over!!Graduate or professional degree"]

# Eduction percentages for 2018
edu_2018_per = ["Estimate!!Percent!!Population 25 years and over!!Less than 9th grade",
                "Estimate!!Percent!!Population 25 years and over!!9th to 12th grade, no diploma",
                "Estimate!!Percent!!Population 25 years and over!!High school graduate (includes equivalency)",
                "Estimate!!Percent!!Population 25 years and over!!Some college, no degree",
                "Estimate!!Percent!!Population 25 years and over!!Associate's degree",
                "Estimate!!Percent!!Population 25 years and over!!Bachelor's degree",
                "Estimate!!Percent!!Population 25 years and over!!Graduate or professional degree"]



"""Age and Sex"""

# 2012 Age and Sex features
age_sex_2012 = ['Total!!Estimate!!Total population',
                'Total!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                'Total!!Estimate!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)',
                'Male!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                'Female!!Estimate!!SUMMARY INDICATORS!!Median age (years)']

# Age and Sex features for 2016
age_sex_2016 = ['Total!!Estimate!!Total population',
                'Total!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                'Total!!Estimate!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)',
                'Male!!Estimate!!SUMMARY INDICATORS!!Median age (years)',
                'Female!!Estimate!!SUMMARY INDICATORS!!Median age (years)']

# Age and Sex features for 2018
age_sex_2018 = ['Estimate!!Total!!Total population',
                'Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Median age (years)',
                'Estimate!!Total!!Total population!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)',
                'Estimate!!Male!!Total population!!SUMMARY INDICATORS!!Median age (years)',
                'Estimate!!Female!!Total population!!SUMMARY INDICATORS!!Median age (years)']




"""Race"""

# 2012 Race features
race_2012_count = ['Estimate!!RACE!!White',
                   'Estimate!!RACE!!Black or African American',
                   'Estimate!!RACE!!American Indian and Alaska Native',
                   'Estimate!!RACE!!Asian',
                   'Estimate!!HISPANIC OR LATINO AND RACE!!Total population']

#  2016 Race features
race_2016_per = ['Percent!!RACE!!One race!!White',
                   'Percent!!RACE!!One race!!Black or African American',
                   'Percent!!RACE!!One race!!American Indian and Alaska Native',
                   'Percent!!RACE!!One race!!Asian',
                   'Percent!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)']

# 2018 Race features
race_2018_per = ['Percent Estimate!!RACE!!Total population!!One race!!White',
                   'Percent Estimate!!RACE!!Total population!!One race!!Black or African American',
                   'Percent Estimate!!RACE!!Total population!!One race!!American Indian and Alaska Native',
                   'Percent Estimate!!RACE!!Total population!!One race!!Asian',
                   'Percent Estimate!!HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)']




"""Income Features"""

# 2012 Income features
income_2012 = ['Households!!Estimate!!Median income (dollars)',
               'Households!!Estimate!!Mean income (dollars)']

# 2016 Income features
income_2016 = ['Households!!Estimate!!Median income (dollars)',
               'Households!!Estimate!!Mean income (dollars)']

# 2018 Income features
income_2018 = ['Estimate!!Households!!Median income (dollars)',
               'Estimate!!Households!!Mean income (dollars)']



"""Miscellaneous"""

# Columns dropped from original dataframe
drop_cols = ['County', 'State', 'Republican', 'Democrat', 'Other', 'Total population',
             'Percent Republican', 'Percent Democrat', 'Percent Other']

states_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
               'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia',
               'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
               'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
               'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
               'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
               'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 
               'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
               'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

Electoral_dict = {'Alabama': 9,
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