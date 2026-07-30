
from services.employee_service import EmployeeService

class Main:
    def __init__(self):
        self.service = EmployeeService()

    def main(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. Display All Employees")
            print("3. Search Employee")
            print("4. Remove Employee")
            print("5. Update Employee")
            print("6. Exit")
            try:
                choice = input("Enter your choice: ")
                switcher = {
                    '1': self.service.add_employee,
                    '2': self.service.display_all,
                    '3': self.service.search_employee,
                    '4': self.service.remove_employee,
                    '5': self.service.update_employee,
                    '6': exit,
                    'default': lambda: print("Invalid choice. Please try again.")
                }
                func = switcher.get(choice, switcher['default'])
                func()
            except ValueError:
                print("Invalid input. Please enter a valid choice.")  
                
if __name__ == "__main__":
    main_program = Main()
    main_program.main()