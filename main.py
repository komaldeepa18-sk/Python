import numpy as np

arr = np.array(12) # OD array
arr1 = np.array([1,2,3,4,5]) #1D array
arr2 = np.array([[1,2,3],
                 [3,4,5]]) #2D array
arr3 = np.array([[[1,2,3],[2,3,4]],
                 [[4,5,6],[5,6,8]]]) #3D array

print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)