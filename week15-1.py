#creation a dictionary with at least five keys and each key represent value as a list where this list contains at least ten values and convert
#this dictionary as a pandas data frame and explore the data through the data frame as follows: 1.apply head() palindrome

import pandas as pd

# Step 1: Create a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jane"],
    "Age": [25, 30, 35, 40, 45, 50, 22, 29, 31, 26],
    "City": ["NY", "LA", "SF", "DC", "Chicago", "Miami", "Boston", "Austin", "Seattle", "Denver"],
    "Score": [85, 90, 78, 88, 92, 75, 84, 79, 94, 77],
    "Palindrome": ["madam", "level", "rotor", "civic", "deified", "radar", "racecar", "noon", "refer", "solos"]
}

# Step 2: Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Explore data with `head()` method
print("First 5 rows of the DataFrame:")
print(df.head())

# Step 4: Check which palindromes in the 'Palindrome' column are valid
df['IsPalindrome'] = df['Palindrome'].apply(lambda x: x == x[::-1])

print("\nDataFrame with Palindrome Check:")
print(df)
