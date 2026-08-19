#Install

# pip install seaborn

# Advantages

# Beautiful plots
# Statistical visualization
# Better defaults
# Works with Pandas

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#First Seaborn Plot

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# sns.lineplot(x=x, y=y)

# plt.show()

#Seaborn with Pandas

# data = {
#     "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
#     "Sales": [100, 150, 120, 180, 200]
# }

# df = pd.DataFrame(data)

# sns.lineplot(data=df,x="Day",y="Sales")
# plt.show()

# hours = [1, 2, 3, 4, 5, 6]
# marks = [45, 50, 60, 65, 75, 85]

# sns.scatterplot(x=hours, y=marks)

# plt.xlabel("Study Hours")
# plt.ylabel("Marks")

# plt.show()

# marks = [45, 50, 55, 60, 60, 65, 70, 70, 75, 80, 85, 90]

# sns.histplot(marks, bins=5)

# plt.title("Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")

# plt.show()

# df = sns.load_dataset("iris")

# sns.pairplot(df)

# plt.show()

# data = {
#     "Age": [20, 25, 30, 35, 40],
#     "Experience": [1, 3, 5, 7, 10],
#     "Salary": [25, 35, 45, 55, 70],
#     "WorkingHours": [8, 9, 8, 10, 9]
# }

# df = pd.DataFrame(data)

# correlation = df.corr()

# print(correlation)
# sns.heatmap(
#     correlation,
#     annot=True
# )

# plt.title("Correlation Heatmap")
# plt.show()
df = sns.load_dataset("titanic")

print(df.head())