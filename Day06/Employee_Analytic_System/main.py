

from analytics import (
    average_salary,
    department_report,
    high_salary,
    sort_salary
)

from utils import(
    load_employee,
    employee_generator
)

employees = load_employee('Day06/Employee_Analytic_System/employees.json')

print("\n Employees")
for emp in employee_generator(employees):
    print(emp)
    
print("\n High Salary")

for emp in high_salary(employees, 50000):
    print(emp)

print("\n Sort Salary")

for emp in sort_salary(employees):
    print(emp)
    
print("\n Department Report")
report = department_report(employees)
for dept, emp_list in report.items():
    print(f"Department: {dept}, Number of Employees: {emp_list}")
print("\n Average Salary")
avg_salary = average_salary(employees)
print(f"{avg_salary:.2f}")