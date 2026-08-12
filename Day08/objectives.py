
# value_counts()
# unique() and nunique()
# duplicated() and drop_duplicates()
# astype()
# String operations with .str
# Date/time operations
# replace()
# map()
# apply() vs vectorization
# query()
# isin()
# between()
# groupby() advanced operations
# agg()
# transform()
# Basic merge()
# Basic concat()
# Data-cleaning workflow


import pandas as pd
import numpy as np

data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": [
        "Rahul", "Amit", "Neha", "Priya",
        "Raj", "Sneha", "Vikas", "Pooja"
    ],
    "Age": [25, 30, 28, 35, 32, np.nan, 40, 29],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "IT", "HR", "Finance", "IT"
    ],
    "Salary": [
        60000, 75000, 85000, 90000,
        95000, 65000, 120000, np.nan
    ],
    "Experience": [
        2, 5, 4, 10, 8, 3, 12, np.nan
    ],
    "JoiningDate": [
        "2024-01-15",
        "2021-06-10",
        "2022-03-20",
        "2016-08-12",
        "2018-11-05",
        "2023-02-18",
        "2014-05-25",
        "2022-09-10"
    ]
}

df = pd.DataFrame(data)

# print(df)

# value_counts()
df['Department'].value_counts()
print(df['Department'].value_counts())

#calculate the percentage of each department
department_percentage = df['Department'].value_counts(normalize=True) * 100
print(department_percentage)

# unique() and nunique()
df['Department'].unique()
print(df['Department'].unique())
df['Department'].nunique()
print(df['Department'].nunique())
# duplicated() and drop_duplicates()
df.duplicated()
print(df['Department'].duplicated())
print(df.duplicated().sum())
print(df.duplicated().any())

print(df['Department'].drop_duplicates())
print(df.drop_duplicates(subset='Department'))
# astype() Data Type Conversion — astype()
print(df['Salary'].astype(str))
df["Department"]=df["Department"].astype("string")
print(df["Department"].str.lower())
# String operations with .str
print(df["Department"].str.lower())
print(df["Department"].str.len())
print(df[df["Department"].str.contains("a",case=False)])
print(df[df["Department"].str.startswith("H")])

print(df["Department"].str.strip)
# Date/time operations
# replace()

df["Department"] = df["Department"].replace({
    "IT Dept": "IT",
    "Information Technology": "IT"
})

# map()

department_code={
    "IT":1,
    "HR":2,
    "Finance":3
}
df["DepartmentCode"]=df["Department"].map(
    department_code
)
print(df["Department"])

# apply() vs vectorization
# query()

df.query("Salary>80000")

print(df["Salary"])

df.query(
    "Age>30 and Salary > 80000"
)

# isin()
df[
    df["Department"].isin(["IT", "Finance"])
]
# between()
df[
    df["Age"].between(25, 35)
]

df[
    df["Salary"].between(70000, 100000)
]
# groupby() advanced operations
df.groupby("Department")["Salary"].agg(
    ["mean", "min", "max", "count"]
)
#Group Multiple Columns
df.groupby(
    ["Department", "Age"]
)["Salary"].mean()


# agg()
#Multiple Aggregations on Different Columns
df.groupby("Department").agg({
    "Salary": ["mean", "max"],
    "Age": ["mean", "min", "max"],
    "Experience": ["mean", "max"]
})

# transform() Important for ML
#transform() is different from groupby().agg().
df["DepartmentAvgSalary"] = (
    df.groupby("Department")["Salary"]
      .transform("mean")
)

dept_data = pd.DataFrame({
    "Department": ["IT", "HR", "Finance"],
    "Manager": [
        "Suresh",
        "Kavita",
        "Anil"
    ]
})

result = pd.merge(
    df,
    dept_data,
    on="Department",
    how="left"
)

#Print Result
print(f" Result Mearge:- ")
print(result)


# Basic merge() Combining DataFrames

# Basic concat()
# Data-cleaning workflow

#Convert Dates
df["JoiningDate"].dtype

df["JoiningDate"] = pd.to_datetime(
    df["JoiningDate"]
)

#Extract Year
df["JoiningYear"]=df["JoiningDate"].dt.year
#print(df)

#Extract Month
df["JoiningMonth"]=df["JoiningDate"].dt.month
#print(df)

#Extract Day
df["JoiningDay"]=df["JoiningDate"].dt.day
print(df)

#Calculate Experience from Joining Date

today=pd.Timestamp.today()

df["YearsSinceJoining"]=(
    (today-df["JoiningDate"]).dt.days/365.25
)
print(df)

