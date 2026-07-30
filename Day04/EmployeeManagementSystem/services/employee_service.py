


from models.employee import Employee
from models.manager import Manager


class EmployeeService:
    def __init__(self):
        self.employees = []
        
    def add_employee(self):
        try:
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            department = input("Enter Employee Department: ")
            salary = float(input("Enter Employee Salary: "))
            employee = Employee(emp_id, name, department, salary)
            self.employees.append(employee)
            print("Employee added successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid salary.")
            
    def display_all(self):
        if len(self.employees) == 0:
            print("No employees to display.")
            return
        for employee in self.employees:
            print(":-------------------------------")
            employee.display()
            
            
    def search_employee(self):
        try:
            emp_id = input("Enter Employee ID to search: ")
            for employee in self.employees:
                if employee.emp_id == emp_id:
                    print("Employee found:")
                    employee.display()
                    return
            print("Employee not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Employee ID.")
    def remove_employee(self):
        try:
            emp_id = input("Enter Employee ID to remove: ")
            for employee in self.employees:
                if employee.emp_id == emp_id:
                    self.employees.remove(employee)
                    print("Employee removed successfully.")
                    return
            print("Employee not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Employee ID.")
            
    def update_employee(self):
        try:
            emp_id = input("Enter Employee ID to update: ")
            for employee in self.employees:
                if employee.emp_id == emp_id:
                    name = input("Enter new Employee Name: ")
                    department = input("Enter new Employee Department: ")
                    salary = float(input("Enter new Employee Salary: "))
                    employee.name = name
                    employee.department = department
                    employee.salary = salary
                    print("Employee updated successfully.")
                    return
            print("Employee not found.")
        except ValueError:
            print("Invalid input. Please enter a valid salary.")

