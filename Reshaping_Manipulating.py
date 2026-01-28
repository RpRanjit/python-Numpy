# Reshaping - array shape /dimension change without modifying data
# arr.reshape()
# total no of elements will be same
'''
Syntax
reshape(rows, columns) specify new shape
if dimension match 

reshape doesn't create a copy it create a view
'''

import numpy as np

arr = np.array([1,2,3,4,5,6])
reshape_arr = arr.reshape(2,3)
print(reshape_arr)


# flattening array
# .ravel() and flatten()
# when you want to multidimensional array into 1d array
# .ravel() -> views
# .flatten() -> copy

arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1.ravel())
print(arr1.flatten())