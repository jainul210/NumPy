#Convert an array of floats [1.1, 2.2, 3.3] into integers.
import numpy as np
arr = np.array([1.1, 2.2, 3.3])
print(arr)
arr1 = arr.astype(np.int32)
print(arr1)