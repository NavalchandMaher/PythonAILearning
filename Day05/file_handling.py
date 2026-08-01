
# File Modes
# r   Read
# w   Write (Overwrite)
# a   Append
# x   Create new file
# rb  Read Binary
# wb  Write Binary


# Rad File

file = open("student.txt", "r")

print(file.read())
file.close()

# Write File
# file =open("student.txt", "w")
# file.write("Hello World")
# file.close()

#Append File
file=open("student.txt", "a")
file.write("\nKomal")
file.close()

#Read Line By Line
file=open("student.txt","r")
for line in file:
    print(line.strip())
file.close()

#5. Best Practice (with)// this is like try with resources in Java. It automatically closes the file after the block is executed, even if an exception occurs.

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())
    
with open("student.txt", "r") as file:
    line_count = len(file.readlines())
    print(line_count)
#print max length of line in file
with open("student.txt", "r") as file:
    max_length = max(len(line) for line in file)
    print(max_length)
    
