import numpy as np

# Example array
arr = [1, 2, 3, 4, 5]

# Find minimum
min_value = min(arr)

# Find maximum
max_value = max(arr)

# Find sum
sum_value = sum(arr)

# Find cumulative sum
cumsum = np.cumsum(arr)  # Using NumPy for cumulative sum

# Output the results
print("Array:", arr)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)
print("Sum of Array:", sum_value)
print("Cumulative Sum:", cumsum.tolist())  # Convert to list for display
