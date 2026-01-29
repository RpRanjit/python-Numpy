# if we are in list the we can add, update in it
# but in array you have to make new ARRAY TO MAKE IT happen
# mean when you change ana array it gives another copy
'''
np.insert(array, index, vlaue, axiz = None)\
array -> original array
index -> where you wnat to do things
value -> something that you want to add of insert
axis -> mainly for 2 or more dimensional
'''

import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)
new_arr = np.insert(arr, 4, 45, axis= None)
print(new_arr)

# in 2d array
arr = arr.reshape(2, 3)
print(arr)
new_arr = np.insert(arr, 1, [25, 35, 45], axis= 0)
print(new_arr)


# append -> add at the end
arr = np.array([10, 20, 30, 40, 50])
print(arr)
new_arr = np.append(arr, 50, axis = None)
print(new_arr)

# we can concatenate means join more tha 1 array
'''
no.concatenate((array1, array2), axis = 0)
axis 0 > vertical stacking
axis 1 > horizontal stacking
'''

arr1 = np.array([30, 40])
arr2 = np.array([50, 60])
# arr1 = np.array([[10, 20], [30, 40]])
# arr2 = np.array([[50, 60], [70, 80]])
new_arr = np.concatenate((arr1, arr2), axis = 0)
print(new_arr)


# deleting an array
'''
np.delete(array, index, axis = None) -> flatten array
it returns new array
'''

arr = np.array([1, 3, 2, 4, 7])
new_arr = np.delete(arr, 3)
print(new_arr)
# for multidimensional array

arr_2d = np.array([[1,2,3],[4,5,6]])
new_arr_2d = np.delete(arr_2d, 0, axis = 0)
print(new_arr_2d)