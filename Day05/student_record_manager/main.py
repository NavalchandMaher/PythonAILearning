


from services.student_service import StudentService

class Main:
    
    def __init__(self):
        self.student_service = StudentService()
        
    def run(self):
        while True:
            print("\nStudent Record Manager")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Remove Student")
            print("5. Update Student")
            print("6. Export Students to CSV")
            print("7. Import Students from CSV")
            print("8. Export Students to JSON")
            print("9. Import Students from JSON")
            print("10. Exit")
            
            choice = input("Enter your choice: ")
            
            try:
                switcher = {
                    '1': self.student_service.add_student_via_input,
                    '2': self.student_service.display_students,
                    '3': self.student_service.search_student,
                    '4': self.student_service.remove_student,
                    '5': self.student_service.update_student,
                    '6': self.student_service.export_students_to_csv,
                    '7': self.student_service.import_students_from_csv,
                    '8': self.student_service.export_json_students,
                    '9': self.student_service.import_json_students,
                    '10': exit,
                    'default': lambda: print("Invalid choice. Please try again.")
                }
                func = switcher.get(choice, switcher['default'])
                func()
            except Exception as e:
                print(f"An error occurred: {e}")
                
if __name__ == "__main__": 
    main = Main()
    main.run()