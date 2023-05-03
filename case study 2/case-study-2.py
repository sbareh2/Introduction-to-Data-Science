# Assessing
# Assessing Data
''''
The files all_alpha_08.csv and all_alpha_18.csv discussed in the previous pages have been provided in the workspace for you here to access. Use pandas to explore these datasets in the Jupyter Notebook below to answer the quiz questions below the notebook about these characteristics of the data:

    number of samples in each dataset
    number of columns in each dataset
    duplicate rows in each dataset
    datatypes of columns
    features with missing values
    number of non-null unique values for features in each dataset
    what those unique values are and counts for each
''''

#Use the space below to explore `all_alpha_08.csv` and `all_alpha_18.csv` to answer the quiz questions below.

import pandas as pd

df_08 = pd.read_csv('all_alpha_08.csv')
df_08.head()


df_18 = pd.read_csv('all_alpha_18.csv')
df_18.head()

df_08.shape

sum(df_08.duplicated())

df_08.info()

df_08.isnull().sum()

df_18.shape

sum(df_18.duplicated())

df_18.isnull().sum()

df_18.info()

df_08.nunique()

df_18.nunique()

df_18.query("Fuel == 'Gasoline'")

df_08.query("Fuel == 'Gasoline'")

df_18.query("Fuel == 'Ethanol/Gas'")

df_08.query("Fuel == 'Ethanol/Gas'")

df_08.query("Fuel == 'Gasoline/Electricity'")

df_18.query("Fuel == 'Gasoline/Electricity'")

df_18.query("Fuel == 'CNG'")

df_08.query("Fuel == 'CNG'")

df_08.query("Fuel == 'Electricity'")

df_18.query("Fuel == 'Electricity'")
----------------------------------------------------------------------------------------------------

