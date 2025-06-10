import numpy as np

#1. Access the 3rd element from a 1D array

arr = np.array([10,20,30,40,50])
arr1 = arr[2]
print("3rd element:",arr1)

#2. Slice a 2D array to get the first two rows

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

two_row = matrix[:2]
print("First two rows:\n",two_row)

# Replace all even numbers in an array with -1

arr = np.array([10,15,20,25,30])
arr[arr % 2 == 0] = -1
print("Even number replaced:",arr)