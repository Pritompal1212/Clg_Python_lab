# Define a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Key to check
key_to_check = "age"  # Change this key to test

# Check if the key exists
if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary with value: {my_dict[key_to_check]}")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")