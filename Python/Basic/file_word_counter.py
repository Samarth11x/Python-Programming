# Question 6: File Word Counter

# 1. SETUP: Create a sample file named 'input.txt' to read from.
sample_content = (
    "This is the first line.\n"
    "This is the second line, which has more words.\n"
    "Finally, a short third line."
)
with open("input.txt", "w") as f:
    f.write(sample_content)

print("Created 'input.txt' with sample content.")
print("-" * 30)

# 2. SOLUTION: Read and count file metrics
def count_file_metrics(filepath):
    """Reads a text file and counts lines, words, and characters."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            
            # Count characters (including whitespace and newlines)
            char_count = len(content)
            
            # Count lines
            line_count = len(content.splitlines())
            
            # Count words (split by whitespace, ignoring empty strings from extra spaces)
            word_count = len(content.split())
            
            print(f"File: {filepath}")
            print(f"Total Lines: {line_count}")
            print(f"Total Words: {word_count}")
            print(f"Total Characters: {char_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")

# Execute the counter function
count_file_metrics("input.txt")
