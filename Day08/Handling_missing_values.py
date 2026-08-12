import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Amit", "Neha", "Priya", "Raj"],
    "Age": [25, np.nan, 28, 35, np.nan],
    "Salary": [60000, 75000, np.nan, 90000, 85000],
    "Department": ["IT", "HR", "IT", np.nan, "IT"]
}

df = pd.DataFrame(data)

print(df)

print("\nHandling missing values:")
#Dropping rows with missing values

#Detecting missing values
print("\nDetecting missing values:")
print(df.isna())

print(df.isna().sum())

print(df.isna().sum().sum())

#Remove rows with missing values
print("\nRemoving rows with missing values:")   
df_cleaned = df.dropna()
print(df_cleaned)