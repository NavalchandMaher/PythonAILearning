college = "ABC College"          # Global Variable


class Student:

    total_students = 0           # Class Variable

    def __init__(self, name, age):
        self.name = name         # Instance Variable
        self.age = age
        Student.total_students += 1

    def display(self):
        self.marks = 95               # Instance Variable
        # marks = 95               # Local Variable

        print("Name :", self.name)
        print("Age :", self.age)
        print("College :", college)
        print("Marks :", self.marks)
        print("Total Students :", Student.total_students)


s1 = Student("Naval", 32)
s2 = Student("Rahul", 25)

s1.display()
print()

s2.display()