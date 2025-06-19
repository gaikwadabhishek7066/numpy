import numpy as np
'''
arr1 = np.arange(1,11)
print("Array from 1 to 10:",arr1)

matrix = np.zeros((3,3))
print("Create 3*3 matrix:",matrix)

matirx1 = np.eye(4)
print("Create 4*4 matrix:",matirx1)

random_array = np.random.rand(5)
print("Random numbers (0-1):",random_array)

even_array = np.arange(2,21,2)
print("Even numbers from 2 to 20:",even_array)

arr = np.array([10,20,30,40,50])
arr1 = arr[2]
print("3rd element:",arr1)

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

arr1 = matrix = matrix[:2]
print("First two rows:\n",arr1)


arr = np.array([1,2,3,4,5,6])
arr[arr % 2 == 0] = -1
print("Replaced evens with -1:",arr)

arr = np.array([10,20,30,40,50])
reversed_arr = arr[::-1]
print("Reversed array:",reversed_arr)

arr = np.array([25,60,45,75,30])
greater = arr[arr > 50]
print("Elements > 50:",greater)


a = np.array([1,2,3])
b = np.array([4,5,6])
sum_array = a + b
print("Element-wise sum:",sum_array)

a = np.array([2,4,6])
b = np.array([1,3,5])
product_array = a * b
print("Element-wise product:",product_array)


arr = np.array([4,9,16,25])
sqrt_array = np.sqrt(arr)
print("Square roots:",sqrt_array)
'''

a = np.array([1,2,3])
b = np.array([4,5,6])
dot_product = np.dot(a,b)
print("Dot_product:",dot_product)