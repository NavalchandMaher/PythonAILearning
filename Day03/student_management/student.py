
# Mini Project (30–45 minutes)

# Build a Student Management System.

# Features
# Add Student
# View Student
# Update Student
# Delete Student
# Search Student
# Exit

# Requirements:

# Use functions
# Use a dictionary
# Use loops
# Handle invalid input with try-except
# Organize helper functions in a separate module if possible


students = {}

def add_student():
    try:
        student_id = input("Enter Student ID: ")
        if student_id in students:
            print("Student ID already exists.")
            return
        name = input("Enter Student Name: ") 
        try:
            age = int(input("Enter Student Age: "))
        except ValueError:
            print("Invalid input. Please enter a valid age.")
            return  
        students[student_id] = {"name": name, "age": age}
        print("Student added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        
def view_students():
    if not students:
        print("No students found.")
        return
    for student_id, details in students.items():
        print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}")
        
def update_student():
    student_id = input("Enter Student ID to update: ")
    if student_id not in students:
        print("Student ID not found.")
        return
    name = input("Enter new Student Name: ")
    try:
        age = int(input("Enter new Student Age: "))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        return
    students[student_id] = {"name": name, "age": age}
    print("Student updated successfully.")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id not in students:
        print("Student ID not found.")
        return
    del students[student_id]
    print("Student deleted successfully.")
def search_student():
    student_id = input("Enter Student ID to search: ")
    if student_id not in students:
        print("Student ID not found.")
        return
    details = students[student_id]
    print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}")

