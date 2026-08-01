
#CSV File Handling
import csv

# Writing to a CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["John", 20, "Math"])
    writer.writerow(["Jane", 22, "Science"])

# Reading from a CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        
        
        
# Dictionary CSV
with open("students_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Course"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "John", "Age": 20, "Course": "Math"})
    writer.writerow({"Name": "Jane", "Age": 22, "Course": "Science"})

with open("students_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

#Serch in CSV
search_name = "John"
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == search_name:
            print(f"Found: {row}")
            break
    else:
        print(f"{search_name} not found in the CSV file.")