# Question 1: Shutil Copy .txt
import os
import shutil
import glob

# Define source and destination folders
SOURCE_DIR = "source_txt_files"
DEST_DIR = "destination_txt_files"

# 1. SETUP: Create necessary folders and dummy files
if os.path.exists(SOURCE_DIR):
    shutil.rmtree(SOURCE_DIR) # Clean up previous run
if os.path.exists(DEST_DIR):
    shutil.rmtree(DEST_DIR)

os.makedirs(SOURCE_DIR)
os.makedirs(DEST_DIR)

# Create a few sample files in the source directory
with open(os.path.join(SOURCE_DIR, "file1.txt"), "w") as f: f.write("Text A")
with open(os.path.join(SOURCE_DIR, "document.txt"), "w") as f: f.write("Text B")
with open(os.path.join(SOURCE_DIR, "config.ini"), "w") as f: f.write("Not copied")
print(f"Setup complete. Created '{SOURCE_DIR}' with 3 files.")
print("-" * 30)

# 2. SOLUTION: Copy .txt files
def copy_txt_files(source, destination):
    """Copies all .txt files from source to destination using shutil."""
    
    # Use glob to find all .txt files in the source directory
    search_pattern = os.path.join(source, "*.txt")
    txt_files = glob.glob(search_pattern)
    
    files_copied = 0
    
    for filepath in txt_files:
        try:
            # os.path.basename extracts just the file name (e.g., 'file1.txt')
            destination_path = os.path.join(destination, os.path.basename(filepath))
            shutil.copy(filepath, destination_path)
            print(f"Copied: {os.path.basename(filepath)}")
            files_copied += 1
        except Exception as e:
            print(f"Error copying {os.path.basename(filepath)}: {e}")

    print(f"\nTotal files copied: {files_copied}")

# Execute the copy function
copy_txt_files(SOURCE_DIR, DEST_DIR)

# Verification (check files in destination folder)
print(f"\nFiles in '{DEST_DIR}': {os.listdir(DEST_DIR)}")
