import numpy as np

'''
arr = np.array([10,20,30,40,50])
print("mean:", arr.mean())
print("Standard Deviation:",arr.std())

print("sum:", arr.sum())
'''
arr = np.arange(1,101)

total_sum = arr.sum()
print("Sum:",total_sum)

total_mean = arr.mean()
print("Mean:",total_mean)

even_number  =arr[arr % 2 == 0]
print("Even Numbers:",even_number)