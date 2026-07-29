
#1. Import Module

import math
print("Square root of 16:",math.sqrt(16))
#2. Import Specific Function

from math import sqrt

print("Square root of 16:",sqrt(16))

#3. Alias

import math as m
print(m.pi)

#4. Built-in Modules

# math
# random
import random
print(random.randint(1, 100))

# datetime
import datetime
print("Current Date and Time:",datetime.datetime.now())

# os
import os
print("Current Working Directory:",os.getcwd())
# sys
import sys
print("Python Version:",sys.version)



