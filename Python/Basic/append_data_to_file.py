# Question 10: Append Data to File

# 1. SETUP: Create a starting file named 'append_file.txt'.
starting_content = "This is the original content of the file.\n"
with open("append_file.txt", "w") as f:
    f.write(starting_content)

print("Created 'append_file.txt' with starting content.")
print("-" * 30)

# 2. SOLUTION: Append data to the file
def append_line_to_file(filepath, new_line):
    """Appends a new line of data to an existing file."""
    
    # Open the file in append mode ('a')
    try:
        with open(filepath, 'a') as file:
            # Write the new line, ensuring a newline character is added
            file.write(new_line + "\n")
            
        print(f"Successfully appended line to '{filepath}'.")
        print(f"Appended line: '{new_line}'")
        
        # Verification: Read and print the entire file content
        with open(filepath, 'r') as file:
            print("\nVerification (Full File Content):")
            print(file.read().strip())
            
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

# The line we want to "simulate" a user entering
user_input_line = "This new sentence was appended successfully."

# Execute the append function
append_line_to_file("append_file.txt", user_input_line)
