'''
Docstring for 6stacking_spliting
stacking
you want to stack the array vertically, horizontally

vstack() row wise
hstack () column wise
'''
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))

# slplitting into various parts
'''
np.split()-> equal
np.hsplit()-> horizontally split
np.vsplit()-> vertically split
make sure the parts are align
'''
arr = np.array([1,2,3,4,5,6])
print(np.split(arr, 3))