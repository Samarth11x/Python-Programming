# Question 5: Compress all files in a folder into a ZIP file
import os
import zipfile
import shutil

TARGET_DIR = "files_to_compress"
ZIP_FILENAME = "archive_output.zip"

# 1. SETUP: Create a folder with several dummy files
if os.path.exists(TARGET_DIR):
    shutil.rmtree(TARGET_DIR)
if os.path.exists(ZIP_FILENAME):
    os.remove(ZIP_FILENAME)
    
os.makedirs(TARGET_DIR)

# Create dummy files
with open(os.path.join(TARGET_DIR, "data.csv"), "w") as f: f.write("1,2,3")
with open(os.path.join(TARGET_DIR, "notes.txt"), "w") as f: f.write("Important notes.")
with open(os.path.join(TARGET_DIR, "readme.md"), "w") as f: f.write("# Readme")

print(f"Setup complete. Created 3 files under '{TARGET_DIR}'.")
print("-" * 30)

# 2. SOLUTION: Compress files using zipfile module
def create_zip_archive(source_folder, output_zip_name):
    """Compresses all files in a source folder into a single ZIP file."""
    
    files_compressed = 0
    
    # Open the ZIP file in write mode ('w')
    with zipfile.ZipFile(output_zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Iterate over all files in the source folder
        for item in os.listdir(source_folder):
            file_path = os.path.join(source_folder, item)
            
            # Ensure we are only trying to zip files, not sub-folders
            if os.path.isfile(file_path):
                # The 'arcname' argument ensures the file inside the zip 
                # is named just by its name, not the full path.
                zipf.write(file_path, arcname=item)
                print(f"Compressed: {item}")
                files_compressed += 1

    print(f"\nSuccessfully created archive: '{output_zip_name}'")
    print(f"Total files compressed: {files_compressed}")

# Execute the function
create_zip_archive(TARGET_DIR, ZIP_FILENAME)

# Verification (check if the zip file exists and is readable)
if os.path.exists(ZIP_FILENAME):
    with zipfile.ZipFile(ZIP_FILENAME, 'r') as zipf:
        print(f"Files inside the ZIP archive: {zipf.namelist()}")
