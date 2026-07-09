# Create a 3-D array and perform operations on it.
import numpy as np
# arr = np.arange(6).reshape(2,3)
# print(arr)
arr = np.arange(27).reshape(3,3,3)

element = arr[1,1,2]
sum = arr.sum(axis=0)
print(sum)