import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# 1. Read CSV
# ==========================================

df = pd.read_csv("Day09/EmployeeAnalyticsSashboard/employees.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistics:")
print(df.describe())


# ==========================================
# 2. Prepare Data
# ==========================================

# Average salary by department
department_salary = (
    df.groupby("Department")["Salary"]
    .mean()
    .sort_values(ascending=False)
)

# Top 10 highest-paid employees
top_10 = (
    df.sort_values(
        by="Salary",
        ascending=False
    )
    .head(10)
)

# Correlation
numeric_df = df.select_dtypes(include="number")
correlation = numeric_df.corr()


# ==========================================
# 3. Create Dashboard
# ==========================================

fig, axes = plt.subplots(
    2,
    3,
    figsize=(18, 10)
)

fig.suptitle(
    "Employee Analytics Dashboard",
    fontsize=20
)


# ==========================================
# Widget 1: Salary Distribution
# ==========================================

sns.histplot(
    data=df,
    x="Salary",
    bins=8,
    kde=True,
    ax=axes[0, 0]
)

axes[0, 0].set_title("Salary Distribution")
axes[0, 0].set_xlabel("Salary")
axes[0, 0].set_ylabel("Employees")


# ==========================================
# Widget 2: Average Salary by Department
# ==========================================

sns.barplot(
    x=department_salary.index,
    y=department_salary.values,
    ax=axes[0, 1]
)

axes[0, 1].set_title("Average Salary by Department")
axes[0, 1].set_xlabel("Department")
axes[0, 1].set_ylabel("Average Salary")


# ==========================================
# Widget 3: Experience vs Salary
# ==========================================

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    ax=axes[0, 2]
)

axes[0, 2].set_title("Experience vs Salary")
axes[0, 2].set_xlabel("Experience (Years)")
axes[0, 2].set_ylabel("Salary")


# ==========================================
# Widget 4: Department-wise Salary
# ==========================================

sns.boxplot(
    data=df,
    x="Department",
    y="Salary",
    ax=axes[1, 0]
)

axes[1, 0].set_title("Salary by Department")
axes[1, 0].set_xlabel("Department")
axes[1, 0].set_ylabel("Salary")


# ==========================================
# Widget 5: Correlation Heatmap
# ==========================================

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Feature Correlation")


# ==========================================
# Widget 6: Top 10 Highest Paid
# ==========================================

sns.barplot(
    data=top_10,
    x="Salary",
    y="Name",
    ax=axes[1, 2]
)

axes[1, 2].set_title("Top 10 Highest-Paid Employees")
axes[1, 2].set_xlabel("Salary")
axes[1, 2].set_ylabel("Employee")


# ==========================================
# 4. Adjust Layout
# ==========================================

plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)


# ==========================================
# 5. Save Complete Dashboard
# ==========================================

plt.savefig(
    "employee_analytics_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)


# ==========================================
# 6. Display Dashboard
# ==========================================

plt.show()