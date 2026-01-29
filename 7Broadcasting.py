# Broadcasting
# If we have to work with millions of data at a time then loop are very slow that where Broacasting comes in handy
# Broadcat is a numpy method/way where we do calculation to diffenet shapes of arrays without using loops

prices = [100, 200, 300]
discount = 10 #10% discount
final_prices = []

for price in prices:
    final_price = price - (price * (discount/100))
    final_prices.append(final_price)
print(final_prices)

# above is loop method
# Now using broadcasting method
import numpy as np
prices = np.array([100, 200, 300])
discount = 10
final_prices = prices - (prices * (discount/100))
print(final_prices)


# How numpy handles arrays of different shapes
# 1. Matching dimensions
# 2. Expanding single eleements
# 3. Incompatible shapes

arr = np.array([10,20,30,40,50,60])
# Expanding single value
arr_2d = arr.reshape(2,3)
arr1 = arr_2d[0]
arr2 = arr_2d[1]
print(arr1,arr2)
result = arr1 * arr2
print(result)

# How to do broadcasting array from 1d to 2d
# explnding the vector
matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([7,8,9])
result = matrix + vector
print(result)

# error
matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([7,8])
result = matrix + vector
print(result)
# in this case we can use reshape
matric = matrix.reshape(3,2)
result = matric + vector
print(result)