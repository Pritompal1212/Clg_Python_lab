# wtite a pyhton program to find largest element among three numbers.

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

    # or shortcut ===== " return max(a, b, c) "
    
# Example usage
num1 = 500
num2 = 565
num3 = 357

largest = find_largest(num1, num2, num3)
print(f"The largest number is: {largest}")