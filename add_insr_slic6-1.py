#write a program to perforam the given operations on a list 1.addition 2.insertion 3.slicing

def list_operations():
    # Initialize a list
    my_list = [10, 20, 30, 40, 50]
    print("Initial List:", my_list)
    
    # 1. Addition: Add an element to the end of the list
    element_to_add = 60
    my_list.append(element_to_add)
    print("After Addition (append 60):", my_list)
    
    # 2. Insertion: Insert an element at a specific index
    index_to_insert = 2
    element_to_insert = 25
    my_list.insert(index_to_insert, element_to_insert)
    print(f"After Insertion (insert 25 at index {index_to_insert}):", my_list)
    
    # 3. Slicing: Extract a sublist
    start_index = 1
    end_index = 4
    sliced_list = my_list[start_index:end_index]
    print(f"Sliced List (from index {start_index} to {end_index - 1}):", sliced_list)

# Call the function
list_operations()
