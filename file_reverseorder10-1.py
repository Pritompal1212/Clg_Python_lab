def print_file_lines_reversed(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove the trailing newline and reverse the line
                reversed_line = line.rstrip()[::-1]
                print(reversed_line)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = 'example.txt'  # Replace with your file name
print_file_lines_reversed(filename)
