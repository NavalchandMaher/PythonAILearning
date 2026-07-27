
from multiprocessing.reduction import duplicate


name="naval"
age=24
address="delhi"
salary=10000.00
is_active = True    

print("Name:",name,"Age:",age,"Address:",address,"Salary:",salary,"Active:",is_active)

#checking the type of variable
print("Type of name:",type(name))
print("Type of age:",type(age))
print("Type of address:",type(address))
print("Type of salary:",type(salary))
print("Type of is_active:",type(is_active))

#Type Conversion
age_str=str(age)
print("Type of age_str:",type(age_str))

print("Type of age:",type(age_str))

#List
#A List is an ordered collection that can be changed (mutable) and allows duplicate values.
fruits=["apple","banana","mango","grapes"]
print("Fruits:",fruits)
fruits.append("orange")
fruits.remove("banana")
fruits.insert(1,"kiwi")
print("Fruits after append and remove:",fruits)

#tuple
#A Tuple is ordered, but cannot be changed (immutable).
fruits_tuple=("apple","banana","mango","grapes","banana")
count=fruits_tuple.count("banana")
print("Count of banana in tuple:",count)
print("Fruits Tuple:",fruits_tuple)

#Dictionary
#A Dictionary stores data as key-value pairs.
student={"name":"naval","age":24,"address":"delhi","salary":10000.00,"is_active":True}
print("Student:",student)
print("Student Name:",student["name"])
student.update({"age":25})
student.pop("salary")
student.update({"salary":12000.00})
print("Student:",student)

#Set
#A Set stores unique values only. No duplicates. Order is not guaranteed.
fruits_set={"apple","banana","mango","grapes"}
print("Fruits Set:",fruits_set)


#Input
# Take Value from User And perform Operation

num1=input("Enter First Number:")
num2=input("Enter Second Number:")  

print(num1+num2)  # This will concatenate the strings

num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
print(num1+num2)  # This will add the numbers10

MAX_VALUE=100
MIN_VALUE=1
print("Max Value:",MAX_VALUE)
print("Min Value:",MIN_VALUE)
