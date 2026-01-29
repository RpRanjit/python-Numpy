# Indexing means selecting a specific element in an array
# while in slicing we can select a portion or multiple elements in an array
# fancy indexing - selcting multiple elements at one time using list of indices
# Boolean Masking- giving certain condition and filtering elements from it


# At first
# How to select an specific element in an array/ access
import numpy as np

'''
array[index] - 1d array
array[row, column] - 2d array
'''

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])
print(arr[3])
print(arr[-1])
# print(arr[10])

arr1 = np.array([[10, 30, 50],
              [20, 40, 60]])

print(arr1[0, 1])
print(arr1[1, 2])


# slicing
'''
array[start:stop:step]
the default value of step is 1
negative step, -1 reverse
'''
arr2 = np.array([10, 20, 30, 40, 50])
print(arr2[0::])
print(arr2[0:3:])
print(arr2[0::2])
print(arr2[::-1])
print(arr2[::-2])
print(arr2[:1:-1])
print(arr2[:0:-1])
print(arr2[3:0:-1])


# Fancy Indexing
# selecting muiltiple elements at once as a list
arr3 = np.array([10, 20, 30, 40, 50, 60])
print(arr3[[0,2,4]])

# Booleaan Masking - giving certain condition and filtering elements from it i.e. True or False
# it is 10 times falster than using loops

print(arr3[arr3 > 25])
