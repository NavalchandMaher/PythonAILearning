import pandas as pd

# Series
# Create a Series with custom indexes.
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# Access elements using labels.
print(s['a'])
# DataFrame
# Create a DataFrame from a dictionary.
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [60000, 70000, 80000, 90000, 100000],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing']
})
# Print the first 10 rows.
print(df.head(10))
# Display column names.
print(df.columns)
# Selection
# Select Name and Salary columns.
print(df[['Name', 'Salary']])
# Print the last 5 rows.
print(df.tail(5))
# Filtering
# Employees with Age > 30.
print(df[df['Age'] > 30])
# Salary between ₹60,000–₹90,000.
print(df[(df['Salary'] >= 60000) & (df['Salary'] <= 90000)])
# Employees in IT department.
print(df[df['Department'] == 'IT'])
# Missing Values
# Count missing values.
print(df.isnull().sum())
# Fill missing salaries with average salary.
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
# GroupBy
# Average salary by department.
print(df.groupby('Department')['Salary'].mean())
# Maximum experience by department.
print(df.groupby('Department')['Experience'].max())
# Merge
# Merge employee and department datasets.
pd.merge(df1, df2, on='Department', how='outer')  # Perform an outer join.
# Perform an outer join.
pd.left(df1, df2, on='Department', how='left')  # Perform a left join.
pd.right(df1, df2, on='Department', how='right')  # Perform a right join.
pd.inner(df1, df2, on='Department', how='inner')  # Perform an inner join.
pd.outer(df1, df2, on='Department', how='outer')  # Perform an outer join.
pd.concat([df1, df2], axis=0)  # Concatenate vertically.