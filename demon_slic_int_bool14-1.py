import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Slicing: Get elements from index 1 to 3 (exclusive of 4)
slice_result = arr[1:4]
print("Basic Slicing (1:4):", slice_result)
# Output: [20 30 40]

# Slicing with step: Get every second element
step_result = arr[::2]
print("Basic Slicing with Step (::2):", step_result)
# Output: [10 30 50]

# Reverse the array
reverse_result = arr[::-1]
print("Reversed Array:", reverse_result)
# Output: [50 40 30 20 10]


# # Create a 2D NumPy array
# arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Access specific elements using their row and column indices
# element = arr2D[1, 2]  # Element at 2nd row, 3rd column
# print("Element at (1,2):", element)
# # Output: 6

# # Access multiple elements: Specify multiple row and column indices
# elements = arr2D[[0, 2], [1, 0]]  # (0,1) and (2,0)
# print("Elements at (0,1) and (2,0):", elements)
# # Output: [2 7]


# Create a NumPy array
# arr = np.array([10, 20, 30, 40, 50])

# # Apply a condition: Get elements greater than 25
# greater_than_25 = arr[arr > 25]
# print("Elements greater than 25:", greater_than_25)
# # Output: [30 40 50]

# # Create a boolean mask
# mask = np.array([True, False, True, False, True])

# # Use the mask to filter elements
# filtered_elements = arr[mask]
# print("Filtered Elements using Boolean Mask:", filtered_elements)
# # Output: [10 30 50]
