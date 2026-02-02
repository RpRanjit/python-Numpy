# why?
# handling missing values efficiently
# np.isnan -> detect missing values
# np.nan_to_num() -> missing values into numbers
# np.isinf() -> to detect infinite values
# NaN -not a number if calculation is wrong or data is missing -True/False


import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])
print(np.isnan(arr))

# we can use this method to only fing the missing values not to compare
# how to replace a data aif it found missing
# np.nan_to_num(array, nan= value) default zero
cleaned_arr = np.nan_to_num(arr, nan = 100)
print(cleaned_arr)

# handling infinite data eg 10^1000
# if return True or False
arr1 = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(arr1))
cleaned_arr = np.nan_to_num(arr1, posinf= 1000, neginf=-1000)
print(cleaned_arr)