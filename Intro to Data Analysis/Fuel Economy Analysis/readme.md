# Welcome to the Data Analysis Process - Case Study 2

In this second case study, you'll be analyzing fuel economy data provided by the EPA, or Environmental Protection Agency.
https://www.epa.gov/compliance-and-fuel-economy-data/data-cars-used-testing-fuel-economy

# Data Overview

We'll learn more about these features as we go. Right now, we have a good idea of what data we're working with, so let's answer some questions. You'll see quick descriptions of each feature again in the next section to help you.
Data Source

Below are the web pages from this video. Note that the datasets we'll be working with are slightly simpler than those found here.

*    EPA Fuel Economy Testing https://www.epa.gov/compliance-and-fuel-economy-data/data-cars-used-testing-fuel-economy
*    DOE Fuel Economy Data https://www.fueleconomy.gov/feg/download.shtml/


# 1. Asking Questions
# Fuel Economy Data

This information is provided by the U.S. Environmental Protection Agency, Office of Mobile Sources, National Vehicle and Fuel Emissions Laboratory.

|Attribute|Description| |-| |Model|Vehicle make and model| |Displ|Engine displacement - the size of an engine in liters| |Cyl|The number of cylinders in a particular engine| |Trans|Transmission Type and Number of Gears| |Drive|Drive axle type (2WD = 2-wheel drive, 4WD = 4-wheel/all-wheel drive)| |Fuel|Fuel Type| |Cert Region*|Certification Region Code| |Sales Area**|Certification Region Code| |Stnd|Vehicle emissions standard code| |Stnd Description*|Vehicle emissions standard description| |Underhood ID |This is a 12-digit ID number that can be found on the underhood emission label of every vehicle. It's required by the EPA to designate its "test group" or "engine family." This is explained more here| |Veh Class|EPA Vehicle Class| |Air Pollution Score|Air pollution score (smog rating)| |City MPG|Estimated city mpg (miles/gallon)| |Hwy MPG|Estimated highway mpg (miles/gallon)| |Cmb MPG|Estimated combined mpg (miles/gallon)| |Greenhouse Gas Score|Greenhouse gas rating| |SmartWay|Yes, No, or Elite| |Comb CO2*|Combined city/highway CO2 tailpipe emissions in grams per mile|
  
  

# 2. Assessing Data

The files all_alpha_08.csv and all_alpha_18.csv discussed in the previous pages have been provided in the workspace for you here to access. Use pandas to explore these datasets in the Jupyter Notebook below to answer the quiz questions below the notebook about these characteristics of the data:

*    number of samples in each dataset
*   number of columns in each dataset
*  duplicate rows in each dataset
* datatypes of columns
*    features with missing values
*    number of non-null unique values for features in each dataset
*    what those unique values are and counts for each


# 3. Cleaning Column Labels
## 1. Drop extraneous columns

Drop features that aren't consistent (not present in both datasets) or aren't relevant to our questions. Use pandas' drop function.
Columns to Drop:

*    From 2008 dataset: 'Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'
*    From 2018 dataset: 'Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'

## 2. Rename Columns

*    Change the "Sales Area" column label in the 2008 dataset to "Cert Region" for consistency.
*    Rename all column labels to replace spaces with underscores and convert everything to lowercase. (Underscores can be much easier to work with in Python than spaces. For example, having spaces wouldn't allow you to use df.column_name instead of df['column_name'] to select columns or use query(). Being consistent with lowercase and underscores also helps make column names easy to remember.)



# 4. Filter, Drop Nulls, Dedupe
## 1. Filter

For consistency, only compare cars certified by California standards. Filter both datasets using query to select only rows where cert_region is CA. Then, drop the cert_region columns, since it will no longer provide any useful information (we'll know every value is 'CA').

## 2. Drop Nulls
Drop any rows in both datasets that contain missing values.

## 3. Dedupe
Drop any duplicate rows in both datasets. 


# 5. Fixing Data Types 
## Fixing Data Types Pt 1

In the next three sections, you'll make the following changes to make the datatypes consistent and practical to work with.
### Fix cyl datatype
*    2008: extract int from string.
*    2018: convert float to int.

### Fix air_pollution_score datatype
*    2008: convert string to float.
*    2018: convert int to float.

### Fix city_mpg, hwy_mpg, cmb_mpg datatypes
*    2008 and 2018: convert string to float.

### Fix greenhouse_gas_score datatype
*    2008: convert from float to int.

## Fixing Data Types Pt 2
Next, you're going to fix the air pollution data type. This one involves a tricky step, and hints are provided along the way.


## Fixing Data Types Part 3

In this last section, you'll fix datatypes of columns for mpg and greenhouse gas score.

After you complete these final fixes, check the datatypes of all features in both datasets to confirm success for all the changes we specified earlier. Here they are again for your reference:
### Fix cyl datatype

*    2008: extract int from string.
*    2018: convert float to int.

### Fix air_pollution_score datatype

*    2008: convert string to float.
*    2018: convert int to float.

### Fix city_mpg, hwy_mpg, cmb_mpg datatypes

*    2008 and 2018: convert string to float.

### Fix greenhouse_gas_score datatype

*    2008: convert from float to int.

# 6. Conclusions & Visuals

Draw conclusions and create visuals to communicate results in the Jupyter notebook below! Make sure to address the following questions.

* Q1: Are more unique models using alternative fuels in 2018 compared to 2008? By how much?
* Q2:  How much have vehicle classes improved in fuel economy (increased in mpg)?
* Q3: What are the characteristics of SmartWay vehicles? Have they changed over time? (mpg, greenhouse gas)
* Q4: What features are associated with better fuel economy (mpg)?

