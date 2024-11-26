#write a program to count the numbers of vowels in a stirng (no control flow allowed)

#here using sum & map func

# def count_vowels(s):
#     # List of vowels
#     vowels = "aeiouAEIOU"
    
#     # Use a list comprehension to filter vowels and calculate the length
#     return sum(map(s.lower().count, vowels))

# Example usage
# string = "Hello World, Python is Amazing!"
# vowel_count = count_vowels(string)
# print("Number of vowels:", vowel_count)


#here using lambda func

# from functools import reduce  # Import reduce

# def count_vowels(s):
#     vowels = "aeiouAEIOU"  # List of vowels
#     # Use reduce to calculate the count of vowels
#     return reduce(lambda acc, char: acc + (1 if char in vowels else 0), s, 0)

# # Test the string
# string = "Where and how many vowels?"
# vowel_count = count_vowels(string)
# print("Number of vowels:", vowel_count)



#write a program to count the numbers of vowels in a stirng (no control flow allowed)
#here using manually

def count_vowels(s):
    vowels = "aeiouAEIOU"  # List of vowels
    count = 0  # Initialize a counter
    
    # Access each character using index and check if it's a vowel
    index = 0
    while index < len(s):
        count += (vowels.find(s[index]) != -1)  # Increment count if the character is a vowel
        index += 1
    
    return count

# Example usage
string = "Hello World, Python is Amazing!"
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)
