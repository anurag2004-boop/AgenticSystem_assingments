import pandas as pd
# Step 1: Create a sample dataset and save it as a CSV file
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
df.to_csv('sample_dataset.csv', index=False)
# Step 2: Load the dataset using pd.read_csv()
print("Loading the dataset...")
df = pd.read_csv('sample_dataset.csv')
print("Dataset loaded successfully!")
# Step 3: Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())
# Step 4: Display the summary statistics of the dataset
print("Summary statistics of the dataset:")
print(df.describe())
# Step 5: Display the data types of each column
print("Data types of each column:")
print(df.dtypes)
# Step 6: Display the number of missing values in each column
print("Number of missing values in each column:")
print(df.isnull().sum())
# Step 7: Display the unique values in the 'City' column
print("Unique values in the 'City' column:")
print(df['City'].unique())
# Step 8: Display the count of unique values in the 'City' column
print("Count of unique values in the 'City' column:")
print(df['City'].value_counts())
# Step 9: Display the mean age of the dataset
print("Mean age of the dataset:")
print(df['Age'].mean())
# Step 10: Display the maximum age in the dataset
print("Maximum age in the dataset:")
print(df['Age'].max())
# Step 11: Display the minimum age in the dataset
print("Minimum age in the dataset:")
print(df['Age'].min())
# Step 12: Display the standard deviation of the age column
print("Standard deviation of the age column:")
print(df['Age'].std())
# Step 13: Display the correlation between age and city (if applicable)
# Note: Correlation is not applicable for categorical data like 'City', so we will skip this step.
# Step 14: Display the first 3 rows of the dataset
print("First 3 rows of the dataset:")
print(df.head(3))
# Step 15: Display the last 2 rows of the dataset
print("Last 2 rows of the dataset:")
print(df.tail(2))
# Step 16: Display the shape of the dataset
print("Shape of the dataset:")
print(df.shape)
# Step 17: Display the column names of the dataset
print("Column names of the dataset:")
print(df.columns)
# Step 18: Display the index of the dataset
print("Index of the dataset:")
print(df.index)
# Step 19: Display the data types of each column
print("Data types of each column:")
print(df.dtypes)
# Step 20: Display the number of unique values in each column
print("Number of unique values in each column:")
print(df.nunique())
# Step 21: Display the count of each unique value in the 'City' column
print("Count of each unique value in the 'City' column:")
print(df['City'].value_counts())
# Step 22: Display the mean age for each city
print("Mean age for each city:")
print(df.groupby('City')['Age'].mean())
# Step 23: Display the count of people in each city
print("Count of people in each city:")
print(df['City'].value_counts())
# Step 24: Display the age of the oldest person in each city

print("Age of the oldest person in each city:")
print(df.groupby('City')['Age'].max())
# Step 25: Display the age of the youngest person in each city
print("Age of the youngest person in each city:")
print(df.groupby('City')['Age'].min())
# Step 26: Display the standard deviation of age for each city
print("Standard deviation of age for each city:")
print(df.groupby('City')['Age'].std())
# Step 27: Display the total number of people in the dataset
print("Total number of people in the dataset:")
print(df.shape[0])
# Step 28: Display the total number of unique cities in the dataset
print("Total number of unique cities in the dataset:")
print(df['City'].nunique())
# Step 29: Display the total number of unique names in the dataset
print("Total number of unique names in the dataset:")

print(df['Name'].nunique())
# Step 30: Display the count of each unique name in the dataset
print("Count of each unique name in the dataset:")
print(df['Name'].value_counts())
