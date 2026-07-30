
from models.employee import Employee

class Manager(Employee):
    def __init__(self, emp_id, name, department, salary, team_size):
        super().__init__(emp_id, name, department, salary)
        self.team_size = team_size

    
    def display(self):
        super().display()
        print(f"Team Size :{self.team_size}")
        return ""