#check whether  a JSON string contains
import json

# JSON string
json_string = '{"name": "Alice", "age": 25, "city": "New York", "skills": ["Python", "JavaScript"]}'

# Parse the JSON string
data = json.loads(json_string)

# Check if a key exists
if "age" in data:
    print("Key 'age' exists!")

# Check if a value exists
if "Alice" in data.values():
    print("Value 'Alice' exists!")

# Check if a specific item exists in a list within the JSON
if "Python" in data.get("skills", []):
    print("Value 'Python' exists in skills!")

# Check if both key and value exist
if data.get("city") == "New York":
    print("Key 'city' has the value 'New York'!")



#demonstrate NumPy arrays creation using array() func
#demonstrateto use of ndim, shape, size, dtype
#demonstrate basic slicing, integer and boolean indexing
#find min, max, sum, cumulative sum of array

#creation a dictionary with at least five keys and each key represent value as a list where this list contains at least ten values and convert
#this dictionary as a pandas data frame and explore the data through the data frame as follows: 1.apply head() palindrome