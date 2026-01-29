
List1 = [1,2,3]
List2 = [4,5,6]
# List comprehension it will be slow when we use large list
result = [x+y for x,y in zip(List1, List2)]
print(result)

# using fast vectorize approach
import numpy as np
# this method is 100 times faster than loops
# use in AI and Machine learning
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = arr1 +arr2
print(result)

arr = np.array([10,20,30])
multiplies = arr*3
print(multiplies)

# Broadcasting -> It exopands smaller array to larger to mantain the shape of array
# faster than loops
# to change the shapes

# Vecorization -> It applies in entire array 
# 100 times faster than loops
# in matrix calculation and methods