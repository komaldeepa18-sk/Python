import numpy as np

arr = np.array([1,2,3,4,5])
arr1 = arr.copy()
arr[0]=6
arr1[2]=8
print("original array", arr)
print("copied array", arr1)

arr2= arr.view()
arr[0]=10
print("original array", arr)
print("viewed array", arr2)