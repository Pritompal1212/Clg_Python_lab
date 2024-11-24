# write a program to perform any 5 built-in function by taking any list
def demonstrate_list_functions():
    # Define a sample list
    my_list = [10, 20, 30, 40, 50, 10]

    print("Original List:", my_list)

    # 1. len(): Get the length of the list
    length = len(my_list)
    print("Length of the List:", length)

    # 2. max(): Find the maximum value in the list
    maximum = max(my_list)
    print("Maximum Value in the List:", maximum)

    # 3. min(): Find the minimum value in the list
    minimum = min(my_list)
    print("Minimum Value in the List:", minimum)

    # 4. count(): Count the occurrences of a specific element
    count_10 = my_list.count(10)
    print("Occurrences of 10 in the List:", count_10)

    # 5. reverse(): Reverse the list
    my_list.reverse()
    print("Reversed List:", my_list)

# Call the function
demonstrate_list_functions()
