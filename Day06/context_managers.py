

with open("Day06/file.txt", "r") as file:
    print(file.read())
    
class Database:
    def __enter__(self):
        print("Connected")
        
    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnected")

with Database() as db:
    print("Performing database operations...")