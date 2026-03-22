import pandas as pd 

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')
# Display the first few rows of the DataFrame
print(df.head())
# Display the column names of the DataFrame
print(df.columns)   
# Display the data types of each column
print(df.dtypes)
# Display summary statistics for the DataFrame
print(df.describe())
# Display the number of rows and columns in the DataFrame
print(df.shape)
# Display the number of unique values in each column
print(df.nunique())
# Display the number of missing values in each column
print(df.isnull().sum())
# Display the unique values in the 'category' column
print(df['category'].unique())
# Display the value counts for the 'category' column
print(df['category'].value_counts())
# Display the correlation matrix for the numerical columns
print(df.corr())

