#Use boolean masking to filter numbers greater than 50 in an array.
import numpy as np
arr = np.array([22,464,84,3,94,3,88,45])
mask = arr > 50
print(arr[mask])