import numpy as np

#1. Create a NumPy array of numbers from 1 to 10
arr = np.arange(1,11)
print(arr)

# 2. Create a 3x3 matrix of zeros

zero_matrix = np.zeros((3,3))
print(zero_matrix)

# Create a 4x4 identity matrix

indentity_matrix = np.eye(4)
print(indentity_matrix)

#Generate an array of 5 random numbers between 0 and 1

random_array = np.random.rand(5)
print(random_array)

#5. Create an array with 10 equally spaced numbers between 1 and 100

linspace_array = np.linspace(1,100,10)
print(linspace_array)