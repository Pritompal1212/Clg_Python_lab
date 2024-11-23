def find_length(string):
    count = 0
    for char in string:
        count += 1
    return count

# Example usage
input_string = "Hello, World!"
length = find_length(input_string)
print(f"The length of the string '{input_string}' is: {length}")
