import numpy as np
# arr = np.arange(6).reshape(2,3)
# print(arr)
arr = np.arange(27).reshape(3,3,3)

element = arr[1,1,2]
# print(element)
sum = arr.sum(axis=0)
print(sum)