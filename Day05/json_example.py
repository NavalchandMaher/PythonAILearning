
import json

from loagning import logger

student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science"]
}

# Dictionary to JSON string

print(json.dumps(student))  # Convert Python object to JSON string

#json string to Dictionary
student_json = json.dumps(student)
student_dict = json.loads(student_json)  # Convert JSON string back to Python dictionary

logger.info(student_dict)  # Output: {'name': 'John', 'age': 20, 'courses': ['Math', 'Science']}
#Save json to File

with open("student.json", "w") as file:
    json.dump(student, file)  # Write JSON data to file
logger.info("JSON data has been written to student.json")
#Read json from File
with open("student.json", "r") as file:
    student_from_file = json.load(file)  # Read JSON data from file
    logger.info(student_from_file)  # Output: {'name': 'John', 'age': 20, 'courses': ['Math', 'Science']}