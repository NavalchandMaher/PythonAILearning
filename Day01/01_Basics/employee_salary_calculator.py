
emp_name=input("Enter employee name: ")
company=input("Enter company name: ")
experience=int(input("Enter experience in years: "))
salary=float(input("Enter salary: "))

annual_salary=salary*12
tax=annual_salary*10/100
net_salary=annual_salary-tax

print(f"""
      ============Employee Salary Details============
      Employee Name : {emp_name}
      Company       : {company}
      Experience    : {experience} years
      
      monthly Salary : {salary}
      Annual Salary  : {annual_salary}
      Tax Deducted   : {tax}
      Net Salary     : {net_salary}
      ================================================""")
