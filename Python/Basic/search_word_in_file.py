# Question 9: Search Word in File

# 1. SETUP: Create a sample file named 'search_target.txt'.
target_content = (
    "Python is the best language. Python can be used for many things, like web "
    "development. I love Python. PYTHON is great."
)
with open("search_target.txt", "w") as f:
    f.write(target_content)

print("Created 'search_target.txt'.")
print("-" * 30)

# 2. SOLUTION: Search for word occurrences
def search_word_in_file(filepath, search_word):
    """Searches for a word in a file and returns its count (case-insensitive)."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            
            # Convert content and search word to lowercase for case-insensitive search
            content_lower = content.lower()
            search_word_lower = search_word.lower()
            
            # Split the content into words
            words = content_lower.split()
            
            # Count the occurrences of the search word
            # Note: This simple method counts whole words only, which is common for this type of task.
            count = words.count(search_word_lower)
            
            print(f"File searched: {filepath}")
            print(f"Word searched (case-insensitive): '{search_word}'")
            print(f"Occurrences found: {count}")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")

# Execute the search function
search_word_in_file("search_target.txt", "Python")
