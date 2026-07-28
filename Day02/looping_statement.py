#for Loop
for i in range(5):
    print(i) #0,1,2,3,4

for i in range(1,5):
    print(i) #1,2,3,4

for i in range(1,10,2):
    print(i) #1,3,5,7,9
    
for i in range(10,1,-1):
    print(i) #10,9,8,7,6,5,4,3,2

for i in range(1,10):
    if(i%2==0):
        print(i) #2,4,6,8
for i in range(1,10):
    if(i%2!=0):
        print(i) #1,3,5,7,9
        
for i in range(1,10):
    if(i%2==0):
        print(i) #2,4,6,8
    else:
        print(i) #1,3,5,7,9
        
# Q1 print star pattern

for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()
    
#while Loop

i=1
while(i<5):
    print(i) #1,2,3,4
    i+=1
    
#break

for i in range(1,10):
    if(i==5):
        break
    print(i) #1,2,3,4
    
#continue

for i in range(1,10):
    if(i==5):
        continue
    print(i) #1,2,3,4,6,7,8,9

#pass
for i in range(1,10):
    if(i==5):
        pass
    print(i) #1,2,3,4,5,6,7,8,9
    
    
 # Looping Through Collections
 
 #List
 
name=["Naval","Chand","Python"]
for i in name:
    print(i) #Naval,Chand,Python
    
#Dictionary
person={"name":"Naval","age":25,"salary":25000}

for key,value in person.items():
    print(key,value) #name Naval, age 25, salary 25000
    
#Set
fruits={"apple","banana","mango"}

for i in fruits:
    print(i) #apple,banana,mango
    
#Enumerate
fruits=["apple","banana","mango"]
for index1,fruit in enumerate(fruits):
    print(index1,fruit) #0 apple, 1 banana, 2 mango
 
    
    
