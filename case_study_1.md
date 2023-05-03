### The Data Analysis Process - Case Study 1 ###

## Assessing Data ##

import pandas as pd

df_red = pd.read_csv('winequality-red.csv', sep=';')
df_white = pd.read_csv('winequality-white.csv', sep=';')

#How many samples of red wine are there?#

#How many samples of white wine are there?#
#How many columns are in each dataset?#
#Which features have missing values?#
df_red.info()
df_white.info()

#How many duplicate rows are in the white wine dataset?#
#Are duplicate rows in these datasets significant/ need to be dropped?#
sum(df_white.duplicated())

#How many unique values of quality are in the red wine dataset?#
#How many unique values of quality are in the white wine dataset?#
df_red.nunique()
df_white.nunique()

#What is the mean density in the red wine dataset?#
mean = df_red['density'].mean()
print(mean)
