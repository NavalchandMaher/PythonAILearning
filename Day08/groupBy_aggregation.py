
import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Amit", "Neha", "Priya", "Raj"],
    "Age": [25, np.nan, 28, 35, np.nan],
    "Salary": [60000, 75000, np.nan, 90000, 85000],
    "Department": ["IT", "HR", "IT", np.nan, "IT"]
}

#GroupBy & Aggregation
df = pd.DataFrame(data)
print(df)

#Add a new column 'Bonus' to the DataFrame
df['Bonus'] = [5000, 7000, 6000, 8000, 7500]
print("\nDataFrame with Bonus column:") 
print(df)

#Update values in the 'Salary' column based on a condition
df.loc[0, 'Salary'] = 65000  # Update Rahul's salary
print("\nDataFrame after updating Rahul's salary:")
print(df)

#Delete the 'Bonus' column from the DataFrame
df.drop(columns=['Bonus'], inplace=True)
print("\nDataFrame after deleting the Bonus column:")
print(df)

#Rename the 'Department' column to 'Dept'
df.rename(columns={'Department': 'Dept'}, inplace=True)
print("\nDataFrame after renaming the Department column:")
print(df)

#Group the DataFrame by 'Dept' and calculate the mean of 'Age' and 'Salary'
grouped_df = df.groupby('Dept').agg({'Age': 'mean', 'Salary': 'mean'})
print("\nGrouped DataFrame with mean Age and Salary by Dept:")
print(grouped_df)


#Merge & Join
merged_df = pd.merge(df, grouped_df, left_on='Dept', right_index=True, suffixes=('', '_mean'))
print("\nMerged DataFrame:")
print(merged_df)

 #left join
left_joined_df = pd.merge(df, grouped_df, left_on='Dept', right_index=True, how='left', suffixes=('', '_mean'))
print("\nLeft Joined DataFrame:")   
print(left_joined_df)

