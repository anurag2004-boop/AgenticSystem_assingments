

#To perform Exploratory Data Analysis (EDA) on the Iris dataset, I would follow these steps:
#1. Load the dataset and inspect its structure:
 #  - I would use `pd.read_csv()` to load the dataset into a Pandas DataFrame.
  # - To inspect the structure, I would use `df.head()` to view the first few rows and `df.info()` to get an overview of the columns, data types, and non-null counts.
#2. Check column information and missing values:
 #  - I would use `df.isnull().sum()` to check for any missing values in each column.
  # - If there are missing values, I would consider strategies for handling them, such as imputation or removal.
#3. Analyze the distribution of one feature (e.g., petal length):
 #  - I would use `df['petal_length'].describe()` to get summary statistics of the petal length.
  # - To visualize the distribution, I would use Plotly's `px.histogram(df, x='petal_length')` to create a histogram.
#4. Identify possible outliers in the dataset:
 #  - I would use a box plot to identify outliers. In Plotly, I can create a box plot with `px.box(df, y='petal_length')` to visualize the distribution and identify any outliers.
#5. Analyze relationships between variables (e.g., petal length vs petal width):
 #  - I would use a scatter plot to visualize the relationship between two variables. In Plotly, I can create a scatter plot with `px.scatter(df, x='petal_length', y='petal_width')` to explore how these features relate to each other.
#6. Discover insights about different species:
 #  - I would group the data by species and calculate summary statistics for each group using `df.groupby('species').describe()`.
  # - I would also create visualizations to compare the distributions of features across species, such as using `px.box(df, x='species', y='petal_length')` to compare petal lengths across different species.
#By following these steps, I would gain a deeper understanding of the dataset, identify any potential issues, and uncover insights that could inform the development of a machine learning model.

import pandas as pd
import plotly.express as px 
# Load the dataset
df = pd.read_csv("titanic.csv")    
# Inspect the dataset structure
print(df.head())
print(df.info())
# Check for missing values
print(df.isnull().sum())
# Analyze the distribution of petal length
print(df['petal_length'].describe())
px.histogram(df, x='petal_length')
# Identify possible outliers using a box plot
px.box(df, y='petal_length')
# Analyze relationships between petal length and petal width
px.scatter(df, x='petal_length', y='petal_width')
# Discover insights about different species
print(df.groupby('species').describe())
px.box(df, x='species', y='petal_length')
px.scatter(df, x='petal_length', y='petal_width', color='species')
