import numpy as np
arr = np.array([1,2,3,4,5])

#for i in arr:
#    print(i)

arr1 = np.array([[1,2,3,4,5],[3,4,5,6,7]])

#for i in arr1:
#    for j in i:
#       print(j)

arr2 = np.array([[[1,2,3],[5,6,7]],[[1,3,4],[8,9,10]]])

for x in np.nditer(arr2):
    print(x)
