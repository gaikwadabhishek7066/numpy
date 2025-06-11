import numpy as np 
'''
arr = np.arange(1,101)
print(arr)

arr = np.zeros((5,5), dtype=int)
arr[0, :] = arr[-1, :] = arr[:, 0] = arr[:, -1] = 1
print(arr)


arr = np.array([1,2,3,4,5])
reversed_arr = arr[::-1]
print(reversed_arr)

arr = np.arange(1,21)
even_number = arr[arr % 2 == 0]
print(even_number)


arr = np.arange(1,10)
matrix = arr.reshape(3,3)
print(matrix)


rolls = np.random.randint(1,7, size=10)
counts = np.bincount(rolls)[1:]
print(counts)


arr = np.array([10,20,30,40,50])
norm = (arr - arr.min()) / (arr.max() - arr.min())
print(norm)


arr = np.arange(10)
np.random.shuffle(arr)
print(arr)


arr = np.arange(1,11)
arr[arr % 2 == 1] = -1
print(arr)


arr = np.array([1,2,3,4,5])
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)

print(mean,median,std)
'''