import pandas as pd
# Step 1: Create a sample dataset and save it as a CSV file
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Score': [85, 90, 78, 92, 88],
    'Label': ['A', 'A', 'B', 'A', 'B']
}
df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)       
# Step 2: Load the dataset using pd.read_csv()
print("Loading the dataset...")
df = pd.read_csv("sample_data.csv")
print("Dataset loaded successfully!")
# Step 3: Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())
# Step 4: Display the last 5 rows of the dataset
print("Last 5 rows of the dataset:")
print(df.tail())
# Step 5: Display the structural information of the dataset
print("Structural information of the dataset:")
print(df.info())
# Step 6: Display the summary statistics of the dataset
print("Summary statistics of the dataset:")
print(df.describe())
# Step 7: Select a single column and store it in a variable
age_column = df['Age']
print("Selected 'Age' column:")
print(age_column)
# Step 8: Select multiple columns and store them in a new DataFrame
selected_columns = df[['Name', 'Score']]
print("Selected 'Name' and 'Score' columns:")
print(selected_columns)
# Step 9: Filter rows based on a numerical condition (Score > 80)
filtered_rows = df[df['Score'] > 80]
print("Filtered rows (Score > 80):")
print(filtered_rows)
