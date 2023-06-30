# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
    return word_count

input_file = "input.txt"
output_file = "output.txt"

# Count the number of words in the input file
num_words = count_words(input_file)

# Write the count to the output file
with open(output_file, 'w') as file:
    file.write(f"Number of words: {num_words}")

print("Count written to output file successfully!")