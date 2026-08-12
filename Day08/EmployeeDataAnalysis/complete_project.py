import pandas as pd


# ==========================================
# 1. Load CSV
# ==========================================

df=pd.read_csv('Day08/EmployeeDataAnalysis/employees.csv')


# ==========================================
# 2. Display First & Last Records
# ==========================================

print("===== FIRST 5 RECORDS =====")
print(df.head())

print("\n===== LAST 5 RECORDS =====")
print(df.tail())


# ==========================================
# 3. Dataset Information
# ==========================================

print("\n===== DATASET INFORMATION =====")
print("Shape:", df.shape)
print("Columns:", list(df.columns))

print("\nData Types:")
print(df.dtypes)

print("\nDataset Info:")
df.info()


# ==========================================
# 4. Check Missing Values
# ==========================================

print("\n===== MISSING VALUES =====")
print(df.isna().sum())


# ==========================================
# 5. Handle Missing Values
# ==========================================

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)

df["Experience"] = df["Experience"].fillna(
    df["Experience"].median()
)


print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isna().sum())


# ==========================================
# 6. Salary > 80,000
# ==========================================

high_salary = df[
    df["Salary"] > 80000
]

print("\n===== SALARY > ₹80,000 =====")
print(high_salary)


# ==========================================
# 7. Department-wise Average Salary
# ==========================================

avg_salary = df.groupby(
    "Department"
)["Salary"].mean()

print("\n===== AVERAGE SALARY BY DEPARTMENT =====")
print(avg_salary)


# ==========================================
# 8. Highest Paid Employee
# ==========================================

highest_paid = df.loc[
    df["Salary"].idxmax()
]

print("\n===== HIGHEST PAID EMPLOYEE =====")
print(highest_paid)


# ==========================================
# 9. Youngest Employee
# ==========================================

youngest = df.loc[
    df["Age"].idxmin()
]

print("\n===== YOUNGEST EMPLOYEE =====")
print(youngest)


# ==========================================
# 10. Oldest Employee
# ==========================================

oldest = df.loc[
    df["Age"].idxmax()
]

print("\n===== OLDEST EMPLOYEE =====")
print(oldest)


# ==========================================
# 11. Add Bonus
# ==========================================

df["Bonus"] = df["Salary"] * 0.10


# ==========================================
# 12. Total Compensation
# ==========================================

df["TotalCompensation"] = (
    df["Salary"] + df["Bonus"]
)


# ==========================================
# 13. Sort by Salary
# ==========================================

df = df.sort_values(
    "Salary",
    ascending=False
)


# ==========================================
# 14. Export Cleaned Dataset
# ==========================================

df.to_csv(
    "cleaned_employees.csv",
    index=False
)

print("\nCleaned dataset exported successfully.")


# ==========================================
# 15. Generate Summary Report
# ==========================================

with open(
    "Day08/EmployeeDataAnalysis/summary_report.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "===== EMPLOYEE DATA ANALYSIS REPORT =====\n\n"
    )

    file.write(
        f"Total Employees: {len(df)}\n"
    )

    file.write(f"Average Salary: ₹{df['Salary'].mean():,.2f}\n")

    file.write(
        f"Maximum Salary: ₹{df['Salary'].max():.2f}\n"
    )

    file.write(
        f"Minimum Salary: ₹{df['Salary'].min():.2f}\n"
    )

    file.write(
        f"Average Age: {df['Age'].mean():.2f}\n"
    )

    file.write(
        "\nDepartment-wise Average Salary:\n"
    )

    for department, salary in avg_salary.items():

        file.write(
            f"{department}: ₹{salary:,.2f}\n"
        )

    file.write(
        "\nHighest Paid Employee:\n"
    )

    file.write(
        f"Name: {highest_paid['Name']}\n"
    )

    file.write(
        f"Salary: ₹{highest_paid['Salary']:,.2f}\n"
    )

    file.write(
        "\nYoungest Employee:\n"
    )

    file.write(
        f"Name: {youngest['Name']}\n"
    )

    file.write(
        f"Age: {youngest['Age']:.0f}\n"
    )

    file.write(
        "\nOldest Employee:\n"
    )

    file.write(
        f"Name: {oldest['Name']}\n"
    )

    file.write(
        f"Age: {oldest['Age']:.0f}\n"
    )

print("Summary report generated successfully.")