

name=input("Enter your name: ")
age=int(input("Enter your age: "))
batch=input("Enter your class: ")
marks=float(input("Enter your marks: "))
address=input("Enter your address: ")

print("---Student Information System---")

# print("Name:",name)
# print("Age:",age)
# print("Batch:",batch)
# print("Marks:",marks)
# print("Address:",address)


print("Name:",name,"Age:",age,"Batch:",batch,"Marks:",marks,"Address:",address)
print(f"Name: {name} Age: {age} Batch: {batch} Marks: {marks} Address: {address}")
print(f"Name: {name} \nAge: {age} \nBatch: {batch} \nMarks: {marks} \nAddress: {address}")  

print(f"Name      : {name}")
print(f"Age       : {age}")
print(f"Batch     : {batch}")
print(f"Marks     : {marks}")
print(f"Address   : {address}")

print(f"""
      This Is Student Information System
      Name      : {name}
      Age       : {age}
      Batch     : {batch}
      Marks     : {marks}
      Address   : {address}
        
      """)

print("Name:",name,"Age:",age,"Batch:",batch,"Marks:",marks,"Address:",address,sep="|")




