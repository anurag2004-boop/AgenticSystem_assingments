import pandas as pd

# --------------------------------------------------
# Create Sample Dataset
# --------------------------------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [92, 78, 88, 95, 67, 90],
    "Passed": [True, True, True, True, False, True],
    "Category": ["A", "B", "A", "A", "C", "B"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# --------------------------------------------------
# Select a single column
# --------------------------------------------------
print("Single Column (Score):")
print(df["Score"])
print("\n")

# --------------------------------------------------
# Select multiple columns and store in new DataFrame
# --------------------------------------------------
selected_columns = df[["Name", "Score"]]

print("New DataFrame with Selected Columns (Name, Score):")
print(selected_columns)
print("\n")

# --------------------------------------------------
# Use iloc to retrieve the first three rows
# --------------------------------------------------
print("First Three Rows using iloc:")
print(df.iloc[:3])
print("\n")

# --------------------------------------------------
# Use loc after setting a meaningful index
# --------------------------------------------------
df_indexed = df.set_index("Name")

print("DataFrame with 'Name' as Index:")
print(df_indexed)
print("\n")

print("Using loc to retrieve data for 'Alice':")
print(df_indexed.loc["Alice"])
print("\n")

# --------------------------------------------------
# Filter rows where Score > 85
# --------------------------------------------------
high_scores = df[df["Score"] > 85]

print("Rows where Score > 85:")
print(high_scores)
print("\n")

# --------------------------------------------------
# Filter rows where Score > 85 AND Passed is True
# --------------------------------------------------
high_passed = df[(df["Score"] > 85) & (df["Passed"] == True)]

print("Rows where Score > 85 AND Passed is True:")
print(high_passed)
print("\n")

# --------------------------------------------------
# Sort the filtered result in descending order of Score
# --------------------------------------------------
sorted_result = high_passed.sort_values(by="Score", ascending=False)

print("Filtered Result Sorted by Score (Descending):")
print(sorted_result)
print("\n")

# --------------------------------------------------
# Chaining filtering and sorting together
# --------------------------------------------------
chained_result = df[(df["Score"] > 85) & (df["Passed"] == True)] \
                    .sort_values(by="Score", ascending=False)

print("Chained Filtering and Sorting Result:")
print(chained_result)
