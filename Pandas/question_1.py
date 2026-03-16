import pandas as pd
import numpy as np
# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [    
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)


# 🔹 Detect and print missing values
print("\nMissing Values in each column:\n")
print(df.isnull().sum())


# 🔹 Fill missing Salary values using column mean
mean_salary = df["Salary"].mean()
df["Salary"].fillna(mean_salary, inplace=True)

print("\nDataFrame after filling missing Salary with mean:\n")
print(df)


# 🔹 Drop Temporary_Notes column
df = df.drop(columns=["Temporary_Notes"])


# 🔹 Rename Salary column to Annual_Salary
df = df.rename(columns={"Salary": "Annual_Salary"})

print("\nDataFrame after cleaning:\n")
print(df)


# 🔹 Group by Department
summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("\nFinal Summary Table:\n")
print(summary)