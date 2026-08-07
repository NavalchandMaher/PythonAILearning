
from decorators import log_operation
from models import Employee

@log_operation
def high_salary(
    employees: list[Employee], threshold: int) -> list[Employee]:
    return [employee for employee in employees if employee.salary > threshold]

@log_operation
def sort_salary(
    employees: list[Employee], descending: bool = True) -> list[Employee]:
    return sorted(employees, key=lambda x: x.salary, reverse=descending)

@log_operation
def department_report(
    employees:list[Employee]):
    return {
        dept:len([emp for emp in employees if emp.department == dept]) 
        for dept in {e.department for e in employees}
    }
   
@log_operation
def average_salary(
    employees: list[Employee]) -> float:
    return sum(e.salary for e in employees) / len(employees) if employees else 0.0
    