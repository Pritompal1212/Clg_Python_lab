#demonstrate NumPy arrays creation using array() func
import numpy as np

# 1. Create a 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1)

# 2. Create a 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2)

# 3. Create a 3D Array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(arr3)

# 4. Create an Array with Specified Data Type
arr4 = np.array([1, 2, 3, 4], dtype='float32')
print("\nArray with Specified Data Type (float32):")
print(arr4)

# 5. Create an Array from a Tuple
arr5 = np.array((10, 20, 30, 40))
print("\nArray Created from a Tuple:")
print(arr5)

# 6. Create an Array with Complex Numbers
arr6 = np.array([1, 2, 3], dtype='complex')
print("\nArray with Complex Numbers:")
print(arr6)

# 7. Create a Boolean Array
arr7 = np.array([0, 1, 2, 3], dtype=bool)
print("\nBoolean Array:")
print(arr7)

# 8. Create an Empty Array (No Elements)
arr8 = np.array([])
print("\nEmpty Array:")
print(arr8)



#demonstrateto use of ndim, shape, size, dtype
#demonstrate basic slicing, integer and boolean indexing
#find min, max, sum, cumulative sum of array

#creation a dictionary with at least five keys and each key represent value as a list where this list contains at least ten values and convert
#this dictionary as a pandas data frame and explore the data through the data frame as follows: 1.apply head() palindrome