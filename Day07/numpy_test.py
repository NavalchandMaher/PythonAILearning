
#introduction to numpy

#install numpy using pip
#pip install numpy
#import numpy as np

# Why NumPy?
# Faster than Python lists
# Memory efficient
# Vectorized operations
# Foundation of AI & Data Science


#Creating NumPy Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

np.zeros((2, 3))  # Create a 2x3 array of zeros
np.ones((3, 2))   # Create a 3x2 array of ones
print(np.zeros((2, 3)))
print(np.ones((3, 2)))

#Identity Matrix
np.eye(3)  # Create a 3x3 identity matrix
print(np.eye(3))

#Even Numbers
even_numbers = np.arange(2, 11, 2)
print(even_numbers)

#Linearly Spaced Values
np.linspace(0, 1, 5)  # Create 5 linearly spaced values between 0 and 1
print(np.linspace(0, 1, 5))


#Array Properties

# Dimension
print(arr.ndim)
print(arr2d.ndim)

# Shape
print(arr.shape)
print(arr2d.shape)

# Size
print(arr.size)
print(arr2d.size)

# Data type
print(arr.dtype)
print(arr2d.dtype)

# Memory usage
print(arr.nbytes)
print(arr2d.nbytes)

#Indexing & Slicing



# One-line revision
# NumPy       → Numerical computing
# ndarray     → N-dimensional array
# Vectorize   → Array operation without Python loop
# Broadcast   → Operations on compatible different shapes
# reshape     → Change shape
# flatten     → 1-D copy
# view        → Shares memory
# copy        → Independent memory
# Masking     → Filter using Boolean conditions
# arange      → Step-based sequence
# linspace    → Fixed-number evenly spaced values
# aggregate   → Summarize data
# shape       → Dimension sizes
# ndim        → Number of dimensions
# concatenate → Existing axis
# stack       → New axis