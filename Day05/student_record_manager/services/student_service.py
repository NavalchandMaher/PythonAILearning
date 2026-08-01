

import logging

from logger import logger

from module.student import Student

class StudentService:
    def __init__(self):
        self.students = []
        
    def add_student_via_input(self):
        try:
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            student = Student(name, age, student_id)
            self.students.append(student)
            print("Student added successfully.")
            logger.info(f"Added student: {student_id}, {name}, {age}")
        except ValueError:
            print("Invalid input. Please enter the correct data types.")
            logger.error("Failed to add student due to invalid input.")

    def display_students(self):
        if len(self.students) == 0:
            print("No students to display.")
            logger.info("No students to display.")
            return
        for student in self.students:
            student.display()
            print("--------------------")
            
    def search_student(self):
        try:
            student_id = input("Enter Student ID to search: ")
            for student in self.students:
                if student.student_id == student_id:
                    print("Student found:")
                    student.display()
                    return
            print("Student not found.")
            logger.info(f"Search for student ID {student_id} - not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Student ID.")
            logger.error("Failed to search student due to invalid input.")
            
    def remove_student(self):
        try:
            student_id = input("Enter Student ID to remove: ")
            for student in self.students:
                if student.student_id == student_id:
                    self.students.remove(student)
                    print("Student removed successfully.")
                    logger.info(f"Removed student: {student_id}")
                    return
            print("Student not found.")
            logger.warning(f"Attempted to remove non-existent student with ID: {student_id}")
        except ValueError:
            print("Invalid input. Please enter a valid Student ID.")
            logger.error("Failed to remove student due to invalid input.")
            
    def update_student(self):
        try:
            student_id = input("Enter Student ID to update: ")
            for student in self.students:
                if student.student_id == student_id:
                    name = input("Enter new Student Name: ")
                    age = int(input("Enter new Student Age: "))
                    student.name = name
                    student.age = age
                    print("Student updated successfully.")
                    logger.info(f"Updated student: {student_id}")
                    return
            print("Student not found.")
            logger.warning(f"Attempted to update non-existent student with ID: {student_id}")
        except ValueError:
            print("Invalid input. Please enter the correct data types.")
            logger.error("Failed to update student due to invalid input.")
            
    def export_students_to_csv(self):
        import csv
        filename ="students_records.csv"
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Age"])
            for student in self.students:
                writer.writerow([student.student_id, student.name, student.age])
        print("Students exported successfully to CSV.")
        logger.info(f"Exported students to CSV file: {filename}")
        
    def import_students_from_csv(self):
        import csv
        try:
            filename = "students_records.csv"
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_id = row["Student ID"]
                    name = row["Name"]
                    age = int(row["Age"])
                    student = Student(name, age, student_id)
                    self.students.append(student)
            print("Students imported successfully from CSV.")
            logger.info(f"Imported students from CSV file: {filename}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            logger.error(f"CSV file '{filename}' not found for import.")
        except KeyError:
            print("CSV file format is incorrect. Please check the headers.")
            logger.error("CSV file format is incorrect. Missing headers.")
        except ValueError:
            print("Invalid data in CSV file. Please check the data types.")
            logger.error("Invalid data in CSV file. Data type mismatch.")
            
    def import_json_students(self):
        import json
        try:
            filename = "students_records.json"
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    student_id = item["student_id"]
                    name = item["name"]
                    age = int(item["age"])
                    student = Student(name, age, student_id)
                    self.students.append(student)
            print("Students imported successfully from JSON.")
            logger.info(f"Imported students from JSON file: {filename}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            logger.error(f"JSON file '{filename}' not found for import.")
        except KeyError:
            print("JSON file format is incorrect. Please check the keys.")
            logger.error("JSON file format is incorrect. Missing keys.")
        except ValueError:
            print("Invalid data in JSON file. Please check the data types.")
            logger.error("Invalid data in JSON file. Data type mismatch.")
            
    def export_json_students(self):
        filename = "students_records.json"
        import json
        data = []
        for student in self.students:
            data.append({
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age
            })
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Students exported successfully to JSON.")    
        logger.info(f"Exported students to JSON file: {filename}")