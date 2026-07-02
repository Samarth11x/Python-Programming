# Question 7: Copy File Content

# 1. SETUP: Create 'source.txt' with content.
source_content = "This content will be copied over to the destination file. It includes a second line.\n"
with open("source.txt", "w") as f:
    f.write(source_content)

print("Created 'source.txt'.")
print("-" * 30)

# 2. SOLUTION: Copy content from source to destination
def copy_file(source_path, dest_path):
    """Copies content from one file to another."""
    try:
        # Open source file in read mode ('r')
        with open(source_path, 'r') as source_file:
            data = source_file.read()
        
        # Open destination file in write mode ('w'). This creates it if it doesn't exist 
        # or overwrites it if it does.
        with open(dest_path, 'w') as dest_file:
            dest_file.write(data)
            
        print(f"Successfully copied content from '{source_path}' to '{dest_path}'.")
        
        # Verification: Read and print the content of the new destination file
        with open(dest_path, 'r') as dest_file:
            print("\nContent of destination.txt:")
            print(dest_file.read().strip())
            
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Execute the copy function
copy_file("source.txt", "destination.txt")
