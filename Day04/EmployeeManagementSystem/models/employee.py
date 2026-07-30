
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(f"ID     :{self.emp_id}")
        print(f"Name   :{self.name}")
        print(f"Dept   :{self.department}")
        print(f"Salary :{self.salary}")
       