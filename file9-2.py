# to sort words in a file and output should have only lower case words from source must be lower lowerd

def sort_words_in_file(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, "r") as file:
            content = file.read()

        # Split the content into words, convert to lowercase, and sort them
        words = content.lower().split()
        sorted_words = sorted(words)

        # Write sorted words to the output file
        with open(output_file, "w") as file:
            file.write("\n".join(sorted_words))
        
        print(f"Words sorted and written to '{output_file}'.")
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = "input.txt"  # Replace with your input file name
output_file = "output.txt"  # Replace with your output file name

# Writing some initial content to the input file for demonstration
with open(input_file, "w") as file:
    file.write("Hello World Python Programming Example Uppercase lowercase")

# Process the file
sort_words_in_file(input_file, output_file)

# Display the output file content
print("\nContent of the output file:")
with open(output_file, "r") as file:
    print(file.read())
