
import matplotlib.pyplot as plt

# Most popular plotting library
# Used in AI, ML, Data Science
# Integrates with NumPy & Pandas

# Introduction to Matplotlib

# Matplotlib is one of the most popular Python libraries for creating data visualizations. It allows you to create a wide variety of plots, such as line charts, bar charts, scatter plots, histograms, pie charts, and more. It is widely used in data science, machine learning, engineering, and scientific research.

# Features of Matplotlib
# Easy to create high-quality graphs and charts.
# Supports both simple and advanced visualizations.
# Highly customizable (colors, labels, styles, fonts, etc.).
# Works well with libraries like NumPy and Pandas.
# Can save plots in multiple formats such as PNG, PDF, SVG, and JPEG.



#Display the plot
#plt.show()

# Common Types of Plots
# Plot Type	           Function	            Use
# Line Plot	       plt.plot()	        Show trends over time
# Bar Chart	       plt.bar()	        Compare categories
# Scatter Plot	   plt.scatter()	    Show relationship between variables
# Histogram	       plt.hist()	        Display data distribution
# Pie Chart	       plt.pie()	        Show proportions
# Box Plot	       plt.boxplot()	    Visualize spread and outliers


#Creating a Simple Line Plot
#Data
x=[1,2,3,4,5]
y=[2,4,6,8,10]

#Create plot
plt.subplot(2, 2, 1)
plt.plot(x,y)

#Add  Labels  and title
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#plt.show()

#Example: Bar Chart

subject=["Math","Science","English"]
marks=[85,90,78]

plt.subplot(2, 2, 2)
plt.bar(subject,marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

#Example: Scatter Plot

x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 7]

plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

#Customizing Plots

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.subplot(2, 2, 4)
# plt.plot(x, y, color="orange", marker="o", linestyle="--", label="Data")
# plt.title("Customized Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
#plt.grid(True)

#Histogram
marks = [70,80,90,95,85,70,60,78]

# plt.subplot(2, 3, 5)
# plt.hist(marks, bins=5)


salary = [30,35,40,42,45,48,100]
plt.subplot(2, 2, 4)
plt.boxplot(salary)

plt.tight_layout()
plt.show()

 