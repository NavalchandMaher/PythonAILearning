
import os

from datetime import datetime

import time

import random

from collections import Counter
import uuid
import os
import datetime
import time
import random
from collections import Counter

from collections import defaultdict

from itertools import combinations, permutations

from functools import reduce

#********************** OS Module **********************
print(os.getcwd())  # Get current working directory

#create folder
os.makedirs("new_folder", exist_ok=True)  # Create a new folder named 'new_folder'

#List files and directories in the current directory
print(os.listdir())  # List all files and directories in the current directory

pathlab = "new_folder"
#Check if a path exists
print(os.path.exists(pathlab))  # Check if the path 'new_folder' exists
#Check if it is a directory
print(os.path.isdir(pathlab))  # Check if 'new_folder' is a directory

#*********************** Datetime Module **********************
# Get current date and time
#print(datetime.now().date())  # Get current date and time

# Format current date and time
#print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # Format current date and time

#*********************** Time Module **********************
# Get current time in seconds since the epoch
print(time.time())  # Get current time in seconds since the epoch
# Get current local time
print(time.localtime())  # Get current local time

time.sleep(1)  # Sleep for 1 second

# ************************* Random Module **********************
# Generate a random integer between 1 and 10
print(random.randint(1, 10))  # Generate a random integer between 1 and 10
# *********************** UUID Module **********************
# Generate a random UUID
print(uuid.uuid4())  # Generate a random UUID


#*********************** Collections Module **********************
# Count the occurrences of each element in a list
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)  # Count the occurrences of each element in the list
print(word_count)  # Print the word count

#*********************** DefaultDict **********************
# Create a defaultdict with a default value of 0
word_count_defaultdict = defaultdict(int)  # Create a defaultdict with a default value of 0
for word in words:
    word_count_defaultdict[word] += 1
print(word_count_defaultdict)  # Print the word count using defaultdict

#*********************** Itertools Module **********************
# Generate all combinations of 2 elements from a list
combs = list(combinations(words, 2))  # Generate all combinations of 2 elements from the list
print(combs)  # Print the combinations

# Generate all permutations of 2 elements from a list
perms = list(permutations(words, 2))  # Generate all permutations of 2 elements from the list
print(perms)  # Print the permutations

#*********************** Functools Module **********************
# Use reduce to calculate the product of a list of numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)  # Calculate the product  

print(product)  # Print the product



