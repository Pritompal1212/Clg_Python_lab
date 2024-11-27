def compute_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_characters = sum(len(line) for line in lines)

        print(f"File: {filename}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_characters}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = 'example1.txt'  # Replace with your file name
compute_file_stats(filename)
