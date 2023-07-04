# Welcome to the Data Analysis Process - Case Study 1

In this first case study, you'll perform the entire data analysis process to investigate a dataset on wine quality. Along the way, you'll explore new ways of manipulating data with NumPy and Pandas, as well as powerful visualization tools with Matplotlib.

We're going to investigate this dataset on physicochemical properties and quality ratings of red and white wine samples. Let's take a closer look at its attributes and pose some questions for our analysis!

https://archive.ics.uci.edu/ml/datasets/Wine+Quality

## Wine Quality Data Set from UCI Machine Learning Lab

There are two datasets that provide information on samples of red and white variants of the Portuguese "Vinho Verde" wine. Each sample of wine was rated for quality by wine experts and examined with physicochemical tests. Due to privacy and logistic issues, only data on these physicochemical properties and quality ratings are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.). (Source https://archive.ics.uci.edu/ml/datasets/Wine+Quality )


## Attributes in Each Dataset:

| #             | 	Physicochemical Properties  | 
| ------------- |:-------------:|
|1              | Fixed Acidity |
|2              | Volatile Acidity |
|3 | Citric Acid     |
4	| Residual Sugar
5	| Chlorides
6	| Free Sulfur Dioxide
7	| Total Sulfur Dioxide
8	| Density
9	| pH
10| Sulphates
11| Alcohol

| #| Quality Rating | 
| -|:-------------:|
|12             | Quality - Score between 0 and 10 (median of at least 3 evaluations made by wine experts) |



# 1. Assessing Data

Using Pandas, explore winequality-red.csv and winequality-white.csv in the Jupyter notebook below to answer quiz questions below the notebook about these characteristics of the datasets:

* number of samples in each dataset
* number of columns in each dataset
* features with missing values
* duplicate rows in the white wine dataset
* number of unique values for quality in each dataset
* mean density of the red wine dataset

# 2. Appending Data

You can combine the red and white datasets to make your analysis more efficient. Use NumPy to create a new column that preserves color information, and then use pandas to combine the dataframes.


## Appending Data (cont.)

Below is the same notebook you worked on in the previous "Appending Data" section. Add a new cell below the first code cell (where you imported packages and loaded data) to fix the problematic column label in the red dataframe.

Use pandas' rename function to change the total_sulfur-dioxide column label to total_sulfur_dioxide. You can check out this Stack Overflow page to help you.

Then, rerun all the cells below that to append the dataframes and save your successfully combined dataset!

# 3. Exploring with Visuals

Use the notebook below to perform exploratory data analysis on your newly combined dataframe. Create some visuals to answer these quiz questions below the notebook.

* Based on histograms of columns in this dataset, which of the following feature variables appear skewed to the right? Fixed Acidity, Total Sulfur Dioxide, pH, Alcohol
* Based on scatterplots of quality against different feature variables, which of the following is most likely to have a positive impact on quality? Volatile Acidity, Residual Sugar, pH, Alcohol.


# 4. Conclusions Using Groupby
# Drawing Conclusions Using Groupby

In the notebook below, you're going to investigate two questions about this data using pandas' groupby function. Here are tips for answering each question:

## Q1: Is a certain type of wine (red or white) associated with higher quality?
For this question, compare the average quality of red wine with the average quality of white wine with groupby. To do this group by color and then find the mean quality of each group.

## Q2: What level of acidity (pH value) receives the highest average rating?
This question is more tricky because unlike color, which has clear categories you can group by (red and white) pH is a quantitative variable without clear categories. However, there is a simple fix to this. You can create a categorical variable from a quantitative variable by creating your own categories. pandas' cut function let's you "cut" data in groups. Using this, create a new column called acidity_levels with these categories:

### Acidity Levels:

1. High: Lowest 25% of pH values
2. Moderately High: 25% - 50% of pH values
3. Medium: 50% - 75% of pH values
4. Low: 75% - max pH value

Here, the data is being split at the 25th, 50th, and 75th percentile. Remember, you can get these numbers with pandas' describe()! After you create these four categories, you'll be able to use groupby to get the mean quality rating for each acidity level.

    
# 5. Conclusions Using Query
# Drawing Conclusions Using Query

In the notebook below, you're going to investigate two questions about this data using pandas' query function. Here are tips for answering each question:

## Q1: Do wines with higher alcoholic content receive better ratings?
To answer this question, use query to create two groups of wine samples:

1. Low alcohol (samples with an alcohol content less than the median)
2. High alcohol (samples with an alcohol content greater than or equal to the median)

Then, find the mean quality rating of each group.

## Q2: Do sweeter wines (more residual sugar) receive better ratings?

Similarly, use the median to split the samples into two groups by residual sugar and find the mean quality rating of each group.

