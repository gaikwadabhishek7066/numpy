import numpy as np

'''
arr = np.array([[10,20,30,40],[50,60,70,80]])
new_arr  =np.insert(arr,2,[1,2,3,4],axis=None)
print(new_arr)
'''
'''
Remoing Element Array

arr =np.array([10,20,30,40,50])
new_arr = np.delete(arr,1)
print(new_arr)

2d Arry Removing

arr_2d = np.array([[10,20,30],[40,50,60]])
new_arr_2d = np.delete(arr_2d,0,axis=0)
print(new_arr_2d)

'''
'''
Stacking

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.vstack((arr1,arr2))) #Vertically
print(np.hstack((arr1,arr2))) #Horizontally
'''
'''
Splitting

arr = np.array([10,20,30,40,50,60])
print(np.split(arr,3))
'''
'''
Broadcasting

prices = np.array([100,200,300])
discount = 10

final_prices = prices - (prices*discount/100)
print(final_prices)

Single Value

arr = np.array([100,200,300])
result = arr * 2
print(result)

1d-to-2d Array

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([10,20,30])
result = matrix+vector
print(result)
'''
'''
Vectorization

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = arr1 + arr2
print(result)

arr = np.array([10,20,30])
multi = arr * 5
print(multi)
'''
'''
Handling Missing & Special Values

isnan
arr = np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))

cleaned_arr = np.nan_to_num(arr)
print(cleaned_arr)

Infinte

arr = np.array([1,2,np.inf,4,np.inf,6])
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr,posinf=100,2)
print(cleaned_arr)

'''
'''
1-d array

arr = np.array([1,2,3])
for x in arr:
    print(x)

2-d array

arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)

for x in arr:
    for y in x:
        print(y)

3-d array

arr = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])

for x in arr:
    print(x)

for x in arr:
    for y in x:
        for z in y:
            print(z)


arr = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])

for x in np.nditer(arr):
    print(x)
'''