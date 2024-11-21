#write a python program to print multiplication table of a given number

# Input the number
number = int(input("Enter a number to display its multiplication table: "))

# Print the multiplication table
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
