#demonstrateto use of ndim, shape, size, dtype

import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Use of ndim
print(f"Number of dimensions (ndim): {arr.ndim}")

# Use of shape
print(f"Shape of the array (shape): {arr.shape}")

# Use of size
print(f"Number of elements (size): {arr.size}")

# Use of dtype
print(f"Data type of elements (dtype): {arr.dtype}")

# Another example with different data types
float_arr = np.array([1.2, 3.4, 5.6])
print(f"Array: {float_arr}")
print(f"Data type of elements (dtype): {float_arr.dtype}")
