import pandas as pd

data = {
    "Name": ["Rahul", "Amit", "Neha", "Priya", "Raj"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [60000, 75000, 80000, 90000, 85000]
}

df = pd.DataFrame(data)

print(df)
print("\nSelecting specific columns:")
selected_columns = df[["Name", "Salary"]]
print(selected_columns)
print("\nSelecting specific rows:")
selected_rows = df.loc[0:2]  # Selecting first three rows
print(selected_rows)
print("\nSelecting specific rows and columns:") 
selected_rows_and_columns = df.loc[0:2, ["Name", "Salary"]]  # Selecting first three rows and specific columns
print(selected_rows_and_columns)

#iloc vs loc
print("\nUsing iloc for selection:")
selected_iloc = df.iloc[0:3, 0:2]  # Selecting first three rows and first two columns
print(selected_iloc)

#loc vs iloc
print("\nUsing loc for selection:")
selected_loc = df.loc[0:2, ["Name", "Salary"]]  # Selecting first three rows and specific columns
print(selected_loc)