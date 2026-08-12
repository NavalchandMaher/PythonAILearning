import pandas as pd

df=pd.read_csv('Day08/EmployeeDataAnalysis/employees.csv')

print("Original DataFrame:")
print(df)

#display first 5 records
print("\nFirst 5 records:")
print(df.head())

#display last 5 records
print("\nLast 5 records:")
print(df.tail())

#Inspect the Dataset
print("\nDataset Shape:")
print(df.shape)

#display column names
print("\nColumn Names:")
print(df.columns.tolist())

#display data types of each column
print("\nData Types:")
print(df.dtypes)

#Dataset Information
print("\nDataset Information:")
print(df.info())

#Handle Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

#Fill missing values in 'Age' column with the mean age
df['Age'] = df['Age'].fillna(df['Age'].median())

#for 'Salary' column, fill missing values with the mean salary
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

#for Experience column, fill missing values with the median experience
df['Experience'] = df['Experience'].fillna(df['Experience'].median())

#Verify that there are no more missing values
print("\nMissing Values After Handling:")
print(df.isnull().sum())

#Filter Salary > 80000

high_salary=df[df['Salary'] > 80000]
print("\nEmployees with Salary greater than 80000:")
print(high_salary)

#Department-Wise Average Salary
dept_avg_salary = df.groupby('Department')['Salary'].mean()
print("\nDepartment-Wise Average Salary:")
print(dept_avg_salary)

#Highest Paid Employee
highest_paid = df.sort_values(by='Salary', ascending=False).head(1) #can use .iloc[0] to get the first row as a Series
print("\nHighest Paid Employee:")
print(highest_paid)

#An even cleaner approach:
highest_paid = df.loc[df['Salary'].idxmax()]
print("\nHighest Paid Employee (using idxmax):")
print(highest_paid)

#Youngest Employee
youngest = df.sort_values(by='Age').head(1)
print("\nYoungest Employee:")
print(youngest)

#OR

youngest = df.loc[df['Age'].idxmin()]
print("\nYoungest Employee (using idxmin):")
print(youngest)

#Oldest Employee
oldest=df.sort_values(by='Age', ascending=False).head(1)
print("\nOldest Employee:")
print(oldest)

#OR

oldest = df.loc[df['Age'].idxmax()]
print("\nOldest Employee (using idxmax):")
print(oldest)

#Add Bonus Column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus Column:")
print(df)

#Add Total Compensation
df['Total_Compensation'] = df['Salary'] + df['Bonus']
print("\nDataFrame with Total Compensation:")
print(df)

#Sort by Salary
df_sorted_salary = df.sort_values(by='Salary', ascending=False)
print("\nDataFrame Sorted by Salary:")
print(df_sorted_salary)

#Export Cleaned Dataset
df.to_csv('Day08/EmployeeDataAnalysis/cleaned_employees.csv', index=False)


#Generate Summary Report
print("\nSummary Report:")

with open("Day08/EmployeeDataAnalysis/summary_report.txt", "w") as f:
    f.write("Summary Report:\n")
    f.write(f"Total Employees: {len(df)}\n")
    f.write(f"Average Age: {df['Age'].mean():.2f}\n")
    f.write(f"Average Salary: {df['Salary'].mean():,.2f}\n")
    f.write(f"Department-Wise Average Salary:\n{dept_avg_salary.to_string()}\n")
    f.write(f"Highest Paid Employee:\n{highest_paid.to_string()}\n")
    f.write(f"Youngest Employee:\n{youngest.to_string()}\n")
    f.write(f"Oldest Employee:\n{oldest.to_string()}\n")