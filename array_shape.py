import numpy as np

arr = np.array([[1,2,3,4],
                [7,8,9,6]])

print(arr.shape)

arr1 = np.array([1,2,3,4,5], ndmin=5)

print(arr1)
print(arr1.shape)