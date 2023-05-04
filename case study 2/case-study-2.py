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
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Cleaning Column Labels
''''
1. Drop extraneous columns
Drop features that aren't consistent (not present in both datasets) or aren't relevant to our questions. Use pandas' drop function.
Columns to Drop:
    From 2008 dataset: 'Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'
    From 2018 dataset: 'Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'

2. Rename Columns
    Change the "Sales Area" column label in the 2008 dataset to "Cert Region" for consistency.
    Rename all column labels to replace spaces with underscores and convert everything to lowercase. (Underscores can be much easier to work with in Python than spaces. For example, having spaces wouldn't allow you to use df.column_name instead of df['column_name'] to select columns or use query(). Being consistent with lowercase and underscores also helps make column names easy to remember.)
''''
# Cleaning Column Labels
Use `all_alpha_08.csv` and `all_alpha_18.csv`

# load datasets
import pandas as pd
df_08 = pd.read_csv('all_alpha_08.csv')
df_18 = pd.read_csv('all_alpha_18.csv')

# view 2008 dataset
df_08.head(1)

# view 2018 dataset
df_18.head(1)

### Drop Extraneous Columns

# drop columns from 2008 dataset
df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1, inplace=True)

# confirm changes
df_08.head(1)

# drop columns from 2018 dataset
df_18.drop(['Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'], axis=1, inplace=True)

# confirm changes
df_18.head()

### Rename Columns

# rename Sales Area to Cert Region
df_08.rename(columns={'Sales Area':'Cert Region'}, inplace=True)

# confirm changes
df_08.head(1)

# replace spaces with underscores and lowercase labels for 2008 dataset
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# confirm changes
df_08.head(1)

# replace spaces with underscores and lowercase labels for 2018 dataset
df_18.rename(columns=lambda x: x.strip().lower().replace(" ","_"), inplace=True)

# confirm changes
df_18.head(1)

# confirm column labels for 2008 and 2018 datasets are identical
df_08.columns == df_18.columns

# make sure they're all identical like this
(df_08.columns == df_18.columns).all()

# save new datasets for next section
df_08.to_csv('data_08_v1.csv', index=False)
df_18.to_csv('data_18_v1.csv', index=False)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Filter, Drop Nulls, Dedupe
''''
1. Filter
For consistency, only compare cars certified by California standards. Filter both datasets using query to select only rows where cert_region is CA. Then, drop the cert_region columns, since it will no longer provide any useful information (we'll know every value is 'CA').

2. Drop Nulls
Drop any rows in both datasets that contain missing values.

3. Dedupe
Drop any duplicate rows in both datasets.
''''
# Filter, Drop Nulls, Dedupe
Use `data_08_v1.csv` and `data_18_v1.csv`. You should've created these data files in the previous section: *Cleaning Column Labels*.

# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08_v1.csv')
df_18 = pd.read_csv('data_18_v1.csv')

# view dimensions of dataset
df_08.shape

# view dimensions of dataset
df_18.shape

## Filter by Certification Region

# filter datasets for rows following California standards
df_08 = df_08.query("cert_region == 'CA'")
df_18 = df_18.query("cert_region == 'CA'")

# confirm only certification region is California
df_08['cert_region'].unique()

# confirm only certification region is California
df_18['cert_region'].unique()

# drop certification region columns form both datasets
df_08.drop(['cert_region'], axis=1, inplace=True)
df_18.drop(['cert_region'], axis=1, inplace=True)

df_08.shape

df_18.shape

## Drop Rows with Missing Values

# view missing value count for each feature in 2008
df_08.isnull().sum()

# view missing value count for each feature in 2018
df_18.isnull().sum()

# drop rows with any null values in both datasets
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)

# checks if any of columns in 2008 have null values - should print False
df_08.isnull().sum().any()

# checks if any of columns in 2018 have null values - should print False
df_18.isnull().sum().any()

## Dedupe Data

# print number of duplicates in 2008 and 2018 datasets
print(sum(df_08.duplicated()))
print(sum(df_18.duplicated()))

# drop duplicates in both datasets
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)

# print number of duplicates again to confirm dedupe - should both be 0
print(sum(df_08.duplicated()))
print(sum(df_18.duplicated()))

# save progress for the next section
df_08.to_csv('data_08_v2.csv', index=False)
df_18.to_csv('data_18_v2.csv', index=False)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Fixing Data Types Pt 1
''''
Fixing Data Types
In the next three sections, you'll make the following changes to make the datatypes consistent and practical to work with.
Fix cyl datatype
    2008: extract int from string.
    2018: convert float to int.
Fix air_pollution_score datatype
    2008: convert string to float.
    2018: convert int to float.
Fix city_mpg, hwy_mpg, cmb_mpg datatypes
    2008 and 2018: convert string to float.
Fix greenhouse_gas_score datatype
    2008: convert from float to int.
In this first part, you'll tackle the first one, fixing the cyl datatype.
''''
# Fixing `cyl` Data Type
#- 2008: extract int from string
#- 2018: convert float to int

#Load datasets `data_08_v2.csv` and `data_18_v2.csv`. You should've created these data files in the previous section: *Filter, Drop Nulls, Dedupe*.

# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08_v2.csv')
df_18 = pd.read_csv('data_18_v2.csv')

# check value counts for the 2008 cyl column
df_08['cyl'].value_counts()

Read [this](https://stackoverflow.com/questions/35376387/extract-int-from-string-in-pandas) to help you extract ints from strings in Pandas for the next step.

# Extract int from strings in the 2008 cyl column
df_08['cyl'] = df_08['cyl'].str.extract('(\d+)').astype(int)

# Check value counts for 2008 cyl column again to confirm the change
df_08['cyl'].value_counts()

# convert 2018 cyl column to int
df_18['cyl'] = df_18['cyl'].astype(int)

df_08.to_csv('data_08_v3.csv', index=False)
df_18.to_csv('data_18_v3.csv', index=False)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Fixing Data Types Part 2
''''
Next, you're going to fix the air pollution data type. This one involves a tricky step, and hints are provided along the way.''''

## Fixing Data Types Pt. 1 ##
"""
2008: extract int from string
2018: convert float to int
"""
# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')

# check value counts for the 2008 cyl column
df_08['cyl'].value_counts()

# Read this to help you extract ints from strings in Pandas for the next step.
# https://stackoverflow.com/questions/35376387/extract-int-from-string-in-pandas
# Extract int from strings in the 2008 cyl column
df_08['cyl'] = df_08['cyl'].str.extract('(\d+)').astype(int)

# Check value counts for 2008 cyl column again to confirm the change
df_08['cyl'].value_counts()

# convert 2018 cyl column to int
df_18['cyl'] = df_18['cyl'].astype(int)

df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Fixing Data Types Pt. 2
"""
2008: convert string to float
2018: convert int to float
"""
# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08_v3.csv')
df_18 = pd.read_csv('data_18_v3.csv')


# try using Pandas to_numeric or astype function to convert the
# 2008 air_pollution_score column to float -- this won't work
df_08['air_pollution_score'].astype(float)

# Figuring out the issue
# Looks like this isn't going to be as simple as converting the datatype.
# According to the error above, the value at row 582 is "6/4" - let's check
# it out.
df_08[df_08.air_pollution_score == '6/4']

# It's not just the air pollution score!
# The mpg columns and greenhouse gas scores also seem to have the same problem -
# maybe that's why these were all saved as strings! This is a little tricky, so
# I'm going to show you how to do it with the 2008 dataset, and then you'll try
# it with the 2018 dataset.

# First, let's get all the hybrids in 2008
hb_08 = df_08[df_08['fuel'].str.contains('/')]
hb_08
# hybrids in 2018
hb_18 = df_18[df_18['fuel'].str.contains('/')]
hb_18

# create two copies of the 2008 hybrids dataframe
df1 = hb_08.copy()  # data on first fuel type of each hybrid vehicle
df2 = hb_08.copy()  # data on second fuel type of each hybrid vehicle

# Each one should look like this
df1

# columns to split by "/"
split_columns = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg',
'cmb_mpg', 'greenhouse_gas_score']

# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])

# this dataframe holds info for the FIRST fuel type of the hybrid
# aka the values before the "/"s
df1

# this dataframe holds info for the SECOND fuel type of the hybrid
# aka the values before the "/"s
df2

# combine dataframes to add to the original dataframe
new_rows = df1.append(df2)

# now we have separate rows for each fuel type of each vehicle!
new_rows

# drop the original hybrid rows
df_08.drop(hb_08.index, inplace=True)

# add in our newly separated rows
df_08 = df_08.append(new_rows, ignore_index=True)

# check that all the original hybrid rows with "/"s are gone
df_08[df_08['fuel'].str.contains('/')]
df_08.shape

# Repeat this process for the 2018 dataset
# create two copies of the 2018 hybrids dataframe, hb_18
df1 = hb_18.copy()
df2 = hb_18.copy()

# Split values for fuel, city_mpg, hwy_mpg, cmb_mpg
# You don't need to split for air_pollution_score or greenhouse_gas_score here
# because these columns are already ints in the 2018 dataset.

# list of columns to split
split_columns = ['fuel','city_mpg','hwy_mpg','cmb_mpg']

# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])

# append the two dataframes
new_rows = df1.append(df2)

# drop each hybrid row from the original 2018 dataframe
# do this by using Pandas drop function with hb_18's index
df_18.drop(hb_18.index, inplace=True)

# append new_rows to df_18
df_18 = df_18.append(new_rows, ignore_index=True)

# check that they're gone
df_18[df_18['fuel'].str.contains('/')]
df_18.shape

# Now we can comfortably continue the changes needed for air_pollution_score!
# Here they are again:
# 2008: convert string to float
# 2018: convert int to float

# convert string to float for 2008 air pollution column
df_08['air_pollution_score'] = df_08['air_pollution_score'].astype(float)

# convert int to float for 2018 air pollution column
df_18['air_pollution_score'] = df_18['air_pollution_score'].astype(float)

df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## Fix `city_mpg`, `hwy_mpg`, `cmb_mpg` datatypes
#   2008 and 2018: convert string to float

# Load datasets `data_08_v4.csv` and `data_18_v4.csv`. You should've created these data files in the previous section: *Fixing Data Types Pt 2*.

# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08_v4.csv')
df_18 = pd.read_csv('data_18_v4.csv')


# convert mpg columns to floats
mpg_columns = ['city_mpg', 'hwy_mpg', 'cmb_mpg']
for c in mpg_columns:
    df_18[c] = df_18[c].astype(float)
    df_08[c] = df_08[c].astype(float)

## Fix `greenhouse_gas_score` datatype
    2008: convert from float to int

# convert from float to int
df_08['greenhouse_gas_score'] = df_08['greenhouse_gas_score'].astype(int)

## All the dataypes are now fixed! Take one last check to confirm all the changes.

df_08.dtypes

df_18.dtypes

df_08.dtypes == df_18.dtypes

# Save your final CLEAN datasets as new files!
df_08.to_csv('clean_08.csv', index=False)
df_18.to_csv('clean_18.csv', index=False)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Exploring with Visuals
''''Use histograms and scatterplots to explore clean_08.csv and clean_18.csv in the Jupyter notebook. Then, answer the quiz questions below the notebook.''''

# load datasets

import pandas as pd
% matplotlib inline
import matplotlib.pyplot as plt
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')

#Compare the distributions of greenhouse gas score in 2008 and 2018.
#How has the distribution of combined mpg changed from 2008 to 2018?
df_08.hist(figsize=(8,8));
df_18.hist(figsize=(8,8));

#Describe the correlation between displacement and combined mpg.
plt.scatter(df_08['displ'], df_08['cmb_mpg'])
plt.xlabel('Engine Displacement (L)')
plt.ylabel('combined MPG')
plt.title('Relationship between Engine displacement and combined mpg')
plt.show();


#Describe the correlation between greenhouse gas score and combined mpg.
plt.show();
plt.scatter(df_08['greenhouse_gas_score'], df_08['cmb_mpg'])
plt.xlabel('Greenhouse Score')
plt.ylabel('Combined MPG')
plt.title('Relationship between Greenhouse Score and combined mpg')
plt.show();

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#Draw conclusions and create visuals to communicate results in the Jupyter notebook below! Make sure to address the following questions.
''''
* Q1: Are more unique models using alternative fuels in 2018 compared to 2008? By how much?
* Q2:  How much have vehicle classes improved in fuel economy (increased in mpg)?
* Q3: What are the characteristics of SmartWay vehicles? Have they changed over time? (mpg, greenhouse gas)
* Q4: What features are associated with better fuel economy (mpg)? ''''

Drawing Conclusions

Use the space below to address questions on datasets clean_08.csv and clean_18.csv. You should've created these data files in the previous section: Fixing Data Types Pt 3.

import pandas as pd

% matplotlib inline

import matplotlib.pyplot as plt

# load datasets
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')
df_08.head(1)

#Q1: Are more unique models using alternative sources of fuel? By how much?
df_08.fuel.value_counts()
df_18.fuel.value_counts()

alt_08 = df_08.query('fuel in ["CNG", "ethanol"]').model.nunique()
alt_08

alt_18 = df_18.query('fuel in ["Ethanol", "Electricity"]').model.nunique()
alt_18

plt.bar(["2008", "2018"], [alt_08, alt_18])
plt.title("Number of Unique Models Using Alternative Fuels")
plt.xlabel("Year")
plt.ylabel("Number of Unique Models");

# total unique models each year
total_08 = df_08.model.nunique()
total_18 = df_18.model.nunique()
total_08, total_18

prop_08 = alt_08/total_08
prop_18 = alt_18/total_18
prop_08, prop_18

plt.bar(["2008", "2018"], [prop_08, prop_18])
plt.title("Proportion of Unique Models Using Alternative Fuels")
plt.xlabel("Year")
plt.ylabel("Proportion of Unique Models");

#Q2: How much have vehicle classes improved in fuel economy?
veh_08 = df_08.groupby('veh_class').cmb_mpg.mean()
veh_08

veh_18 = df_18.groupby('veh_class').cmb_mpg.mean()
veh_18

inc = veh_18 - veh_08
inc

inc.dropna(inplace=True)

plt.subplots(figsize=(8, 5))
plt.bar(inc.index, inc)
plt.title('Improvements in Fuel Economy from 2008 to 2018 by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Increase in Average Combined MPG');

#Q3: What are the characteristics of SmartWay vehicles? Have they changed over time?
df_08.smartway.unique()

smart_08 = df_08.query('smartway == "yes"')
smart_08.describe()

df_18.smartway.unique()

smart_18 = df_18.query('smartway in ["Yes", "Elite"]')

smart_18.describe()

#Q4: What features are associated with better fuel economy?

top_08 = df_08.query('cmb_mpg > cmb_mpg.mean()')
top_08.describe()

top_18 = df_18.query('cmb_mpg > cmb_mpg.mean()')
top_18.describe()
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Merging Datasets

''''Use pandas Merges to create a combined dataset from clean_08.csv and clean_18.csv. You should've created these data files in the previous section: Fixing Data Types Pt 3.''''

# load datasets
import pandas as pd

df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')

df_08.head(1)

#Create combined dataset
# rename 2008 columns
df_08.rename(columns = lambda x: x[:10] + "_2008", inplace=True)

# view to check names
df_08.head()

# merge datasets
df_combined = df_08.merge(df_18, left_on='model_2008', right_on='model', how='inner')

# view to check merge
df_combined.head()

#Save the combined dataset
df_combined.to_csv('combined_dataset.csv', index=False)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Results with Merged Dataset
''''Q5: For all of the models that were produced in 2008 that are still being produced now, how much has the mpg improved and which vehicle improved the most?

Remember to use your new dataset, combined_dataset.csv. You should've created this data file in the previous section: Merging Datasets.''''

# load dataset

import pandas as pd
df = pd.read_csv('combined_dataset.csv')

#1. Create a new dataframe, model_mpg, that contain the mean combined mpg values in 2008 and 2018 for each unique model
#To do this, group by model and find the mean cmb_mpg_2008 and mean cmb_mpg for each.

model_mpg = df.groupby(df['model']).mean()[['cmb_mpg_2008', 'cmb_mpg']]
model_mpg.head()

#2. Create a new column, mpg_change, with the change in mpg
#Subtract the mean mpg in 2008 from that in 2018 to get the change in mpg

model_mpg['mpg_change'] = model_mpg['cmb_mpg'] - model_mpg['cmb_mpg_2008']
model_mpg.head()

# 3. Find the vehicle that improved the most
#Find the max mpg change, and then use query or indexing to see what model it is!

max_mpg_change = model_mpg['mpg_change'].max()
max_mpg_change

model_mpg[model_mpg['mpg_change'] == max_mpg_change]

idx = model_mpg.mpg_change.idxmax()
idx

model_mpg.loc[idx]
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

