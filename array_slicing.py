import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])

print(array[0:5]) # first 5 elements
print(array[3:])
print(array[:5])
print(array[-3:-1])
# slicing with step
print(array[0:8:2])

arr2 = np.array([[1,2,3],
                 [3,4,5]]) #2D array

print(arr2[1, 0:2])