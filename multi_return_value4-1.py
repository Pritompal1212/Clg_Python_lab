def calculate(a, b):
    # Perform basic operations
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None  # Handle division by zero
    
    # Return all results
    return addition, subtraction, multiplication, division

# Example usage
num1 = 10
num2 = 5

# Unpacking the multiple return values
add, sub, mul, div = calculate(num1, num2)

# Display results
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
