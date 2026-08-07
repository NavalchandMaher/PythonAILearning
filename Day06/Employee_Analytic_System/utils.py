import json
from typing import Generator

from models import Employee

def load_employee(filename: str) -> list[Employee]:
    with open(filename, 'r') as file:
        data = json.load(file)
        return [Employee(**item) for item in data]

def employee_generator(
    employees: list[Employee]) -> Generator[Employee, None, None]:
    for employee in employees:
        yield employee