# SQL/Java vs Pandas Quick Reference
# SQL / Java	                       Pandas
# SELECT *	                           df
# SELECT column	                       df["column"]
# WHERE salary > 80000	               df[df["Salary"] > 80000]
# ORDER BY salary DESC	               df.sort_values("Salary", ascending=False)
# GROUP BY department	               df.groupby("Department")
# COUNT(*)	                           df.count() / value_counts()
# JOIN	                               pd.merge()
# Update field	                       df.loc[row, col] = value
# Add column	                       df["NewColumn"] = ...
# Export CSV	                       df.to_csv()