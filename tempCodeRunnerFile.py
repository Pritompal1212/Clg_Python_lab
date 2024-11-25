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
