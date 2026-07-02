# Question 4: os.walk Directory Traversal
import os
import shutil

ROOT_DIR = "traversal_root"

# 1. SETUP: Create a nested directory structure for testing os.walk
if os.path.exists(ROOT_DIR):
    shutil.rmtree(ROOT_DIR)

# Create the structure:
# traversal_root/
# ├── subfolder_a/
# │   └── file_a.txt
# ├── subfolder_b/
# │   └── sub_sub_folder/
# │       └── file_b.py
# └── main_file.log

os.makedirs(os.path.join(ROOT_DIR, "subfolder_a"))
os.makedirs(os.path.join(ROOT_DIR, "subfolder_b", "sub_sub_folder"))

with open(os.path.join(ROOT_DIR, "main_file.log"), "w") as f: f.write("Log")
with open(os.path.join(ROOT_DIR, "subfolder_a", "file_a.txt"), "w") as f: f.write("A")
with open(os.path.join(ROOT_DIR, "subfolder_b", "sub_sub_folder", "file_b.py"), "w") as f: f.write("B")

print(f"Setup complete. Created test structure under '{ROOT_DIR}'.")
print("-" * 30)

# 2. SOLUTION: Traverse and print using os.walk()
def traverse_directory(root_dir):
    """Traverses a directory tree using os.walk and prints folders/files."""
    print(f"Starting traversal of: {root_dir}\n")
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # dirpath: The path to the current directory
        # dirnames: A list of subdirectories in dirpath
        # filenames: A list of files in dirpath
        
        print(f"CURRENT PATH: {dirpath}")
        print(f"  FOLDERS: {dirnames}")
        print(f"  FILES: {filenames}")
        print("-" * 15)

# Execute the traversal function
traverse_directory(ROOT_DIR)
