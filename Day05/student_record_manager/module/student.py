class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display(self):
        print(f"Name      : {self.name}")
        print(f"Age       : {self.age}")
        print(f"Student ID: {self.student_id}")

