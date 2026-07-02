# Question 8: File Extension Checker (os.path)
import os

def analyze_filepath(filepath):
    """Analyzes a given file path to extract its components."""
    
    # Extract directory path
    directory_name = os.path.dirname(filepath)
    
    # Extract the full file name (base name)
    full_file_name = os.path.basename(filepath)
    
    # Split the file name into its base name and extension
    file_base, file_extension = os.path.splitext(full_file_name)
    
    # If a directory is empty, os.path.dirname returns an empty string or '.'
    if not directory_name:
        directory_name = "(Current Directory)"
    
    print("\n--- File Path Analysis ---")
    print(f"Input Path: {filepath}")
    print(f"Directory Name: {directory_name}")
    print(f"File Name (without extension): {file_base}")
    print(f"File Extension: {file_extension}")
    print("--------------------------")

# Example Usage 1 (Absolute Path)
analyze_filepath("/home/user/documents/report.pdf")

# Example Usage 2 (Local Path)
analyze_filepath("data/assignments/submission.py")
