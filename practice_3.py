#Use fancy indexing to extract even numbers from [1, 2, 3, 4, 5, 6].
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
idx = [1,3,5]
print(arr[idx])