import pandas as pd

data = {
    "Name": ["Rahul", "Amit", "Neha", "Priya", "Raj"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [60000, 75000, 80000, 90000, 85000]
}

#Ascending order sorting by Age
df = pd.DataFrame(data)
df = df.sort_values(by="Age", ascending=True)
print(df)
#Descending order sorting by Salary
df = df.sort_values(by="Salary", ascending=False)
print(df)

#Sorting by multiple columns (first by Department, then by Salary)
#df = pd.DataFrame(data)
df = df.sort_values(by=["Department", "Salary"], ascending=[True, False])
print(df)