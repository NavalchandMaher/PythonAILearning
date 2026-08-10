
import numpy as np

# Arrays
# Create a NumPy array from a list.

arr=np.array([1, 2, 3, 4, 5])  # Create a 1D array
print("1 .",arr)

# Create a 4×4 identity matrix.

identity_matrix = np.eye(4)
print("2 .",identity_matrix)
# Create numbers from 10–100 with step 5.
numbers = np.arange(10, 101, 5)
print("3 .",numbers)

# Indexing
matrix=np.arange(1, 17).reshape(4, 4)  # Create a 4x4 matrix
print("4 .",matrix)
# Print the last row.
# Print the second column.
print("5 . Last row:", matrix[:,-1])
print("5 . Second column:", matrix[:,1])
# Reverse an array.
print("6 . Reversed array:", arr[::-1])
# Math
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# Add two arrays.
print("7 . Sum of arrays:", arr1 + arr2)          
# Multiply an array by 5.
print("8 . Array multiplied by 5:", arr * 5)
# Calculate square roots.
print("9 . Square roots:", np.sqrt(arr))
# Statistics
data = np.array([1, 2, 3, 4, 5])    
# Find mean, median, max, min, std.
print("10 . Mean:", np.mean(data))
print("10 . Median:", np.median(data))
print("10 . Max:", np.max(data))
print("10 . Min:", np.min(data))
print("10 . Standard Deviation:", np.std(data))
# Broadcasting
# Add 100 to every element.
print("11 . Array with 100 added:", arr + 100)
# Multiply each row by 2.
print("12 . Matrix with each row multiplied by 2:", matrix * 2)
# Boolean Masking
# Print values greater than 50.
print("13 . Values greater than 50:", data[data > 50])
# Print even numbers only.
print("14 . Even numbers:", data[data % 2 == 0])
# Random
# Generate a random 5×5 matrix.
print("15 . Random 5x5 matrix:", np.random.rand(5, 5))
# Generate 20 random integers between 1–100.
print("16 . 20 random integers between 1–100:", np.random.randint(1, 101, 20))