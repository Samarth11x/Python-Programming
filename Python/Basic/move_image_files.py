# Question 2: Move Image Files
import os
import shutil

IMAGE_DIR = "images"

# 1. SETUP: Create necessary files in the current directory and the destination folder
# Clean up previous run and create destination folder
if os.path.exists(IMAGE_DIR):
    shutil.rmtree(IMAGE_DIR)
os.makedirs(IMAGE_DIR)

# Create dummy files in the current directory
dummy_files = {
    "photo1.jpg": "image",
    "icon.png": "image",
    "document.pdf": "other",
    "script.py": "other",
    "logo.PNG": "image (uppercase extension)"
}
for name in dummy_files:
    with open(name, "w") as f:
        f.write(f"This is a dummy {name}")

print(f"Setup complete. Created 5 files in current directory.")
print("-" * 30)

# 2. SOLUTION: Move image files to 'images' folder
def move_image_files(destination_folder):
    """Moves image files (.jpg, .png) from current dir to destination_folder."""
    
    moved_count = 0
    # List all items in the current directory
    all_items = os.listdir('.')
    
    # Define image extensions (case-insensitive)
    image_extensions = ('.jpg', '.png', '.jpeg') 
    
    for item in all_items:
        # Check if the item is a file (not a folder, like the 'images' folder itself)
        if os.path.isfile(item):
            # Get the file extension and convert to lowercase for case-insensitive check
            file_name, file_ext = os.path.splitext(item)
            if file_ext.lower() in image_extensions:
                source_path = item
                dest_path = os.path.join(destination_folder, item)
                
                try:
                    shutil.move(source_path, dest_path)
                    print(f"Moved: {item}")
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {item}: {e}")

    print(f"\nTotal files moved: {moved_count}")

# Execute the move function
move_image_files(IMAGE_DIR)

# Verification
print(f"Files remaining in current directory (non-images): {os.listdir('.')}")
print(f"Files in '{IMAGE_DIR}' folder: {os.listdir(IMAGE_DIR)}")
