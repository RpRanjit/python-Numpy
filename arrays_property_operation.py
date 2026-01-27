# Properties of numpy
# what calculation can we do fo operations

# How to check the shape, size and type?

# For shape abou rows and column whhile working with multidimensional arrays

import numpy as np

arr_2d = np.array([[1,2,3],
                  [4,5,6]])
print("Shape of an array")
print(arr_2d.shape)

# for size to determine total no of elements in an array
arr = np.array([[23,45,6],
                [10,24,75]])
print("Size of an array")
print(arr.size)

# ndim = to find the no of dimensions
arr_1d = np.array([1,23,3])
arr_2d = np.array([[1,23,3], [3,4,5]])
arr_3d = np.array([[1,23,3], [3,2,5], [9, 0,1]])
print("Dimension of an array")
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

# dtype to find out the datatype of an elements (int, float, str)
arr = np.array([10,20,30.5,40])
print(arr.dtype)

# to change the datatype into different using astype
arr = np.array([10.5, 30.9,33.3])
int_arr= arr.astype(int)
print(int_arr)
print(int_arr.dtype)

# one of the reason we use numpy is because we can do mathmathical operation without using loops
 

arr1 = np.array([10, 20, 30])
print("Mathematical operations")
print(arr1 + 10)
print(arr1 - 10)
print(arr1 * 10)
print(arr1 / 10)
print(arr1 ** 10)
print(arr1 % 10)

# Aggregation function (Summarise)like in pandas
# functions           what it does
# np.sum()             add all
# np.mean()           calculate average
# min(), max()         Give minimum and maximum values
# np.std()              standarg deviation
# np.var()               variance


arr = np.array([10, 20, 30, 40, 50])
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))