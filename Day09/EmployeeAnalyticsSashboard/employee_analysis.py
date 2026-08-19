
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Read CSV
df = pd.read_csv("Day09/EmployeeAnalyticsSashboard/employees.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df["Department"].value_counts())

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Salary",
    bins=8,
    kde=True
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("salary_distribution.png")
plt.show()

#Department Salary Bar Chart

department_salary = df.groupby("Department")["Salary"].mean()

print(department_salary)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=department_salary.index,
    y=department_salary.values
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.savefig("department_salary.png")
plt.show()

#Experience vs Salary

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary"
)

plt.title("Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

plt.tight_layout()
plt.savefig("experience_vs_salary.png")
plt.show()

#Department-wise Box Plot

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Department",
    y="Salary"
)

plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.tight_layout()
plt.savefig("department_salary_boxplot.png")
plt.show()

#Correlation Heatmap

numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()
print(correlation)

plt.figure(figsize=(9, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Employee Feature Correlation")

plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

#Top 10 Highest-Paid Employees

top_10 = df.sort_values(
    by="Salary",
    ascending=False
).head(10)

print(top_10[["Name", "Department", "Salary"]])

plt.figure(figsize=(10, 6))

sns.barplot(
    data=top_10,
    x="Salary",
    y="Name"
)

plt.title("Top 10 Highest-Paid Employees")
plt.xlabel("Salary")
plt.ylabel("Employee")

plt.tight_layout()
plt.savefig("top_10_highest_paid.png")
plt.show()
