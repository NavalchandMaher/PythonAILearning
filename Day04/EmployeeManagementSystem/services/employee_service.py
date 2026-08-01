
from logger import logging

from models.employee import Employee
from models.manager import Manager


class EmployeeService:
    def __init__(self):
        self.employees = []
        logging.info("EmployeeService initialized with an empty employee list.")
        
    def add_employee(self):
        try:
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            department = input("Enter Employee Department: ")
            salary = float(input("Enter Employee Salary: "))
            employee = Employee(emp_id, name, department, salary)
            self.employees.append(employee)
            print("Employee added successfully.")
            logging.info(f"Employee added: {employee.emp_id} - {employee.name}")
        except ValueError:
            print("Invalid input. Please enter a valid salary.")
            logging.error("Invalid salary input while adding employee.")
            
    def display_all(self):
        if len(self.employees) == 0:
            print("No employees to display.")
            logging.info("No employees to display.")
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
            logging.error("Invalid Employee ID input while searching employee.")
    def remove_employee(self):
        try:
            emp_id = input("Enter Employee ID to remove: ")
            for employee in self.employees:
                if employee.emp_id == emp_id:
                    self.employees.remove(employee)
                    print("Employee removed successfully.")
                    logging.info(f"Employee removed: {employee.emp_id} - {employee.name}")
                    return
            print("Employee not found.")
            logging.warning(f"Attempted to remove non-existent employee with ID: {emp_id}")
        except ValueError:
            print("Invalid input. Please enter a valid Employee ID.")
            logging.error("Invalid Employee ID input while removing employee.")
            
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
                    logging.info(f"Employee updated: {employee.emp_id} - {employee.name}")
                    return
            print("Employee not found.")
            logging.warning(f"Attempted to update non-existent employee with ID: {emp_id}")
        except ValueError:
            print("Invalid input. Please enter a valid salary.")
            logging.error("Invalid salary input while updating employee.")

