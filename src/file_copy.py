import os
import shutil

def copy_file(source_path, destination_path):
    """
    Copy a file from source path to destination path.
    
    Args:
        source_path (str): Path to the source file to be copied.
        destination_path (str): Path where the file should be copied to.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are permission issues with reading/writing.
        IsADirectoryError: If source or destination is a directory instead of a file.
        ValueError: If source or destination paths are invalid or empty.
    """
    # Validate input paths
    if not source_path or not destination_path:
        raise ValueError("Source and destination paths cannot be empty.")
    
    # Normalize paths to handle relative paths
    source_path = os.path.abspath(source_path)
    destination_path = os.path.abspath(destination_path)
    
    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Check if source is a file
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path must be a file: {source_path}")
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Copy the file
    try:
        shutil.copy2(source_path, destination_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when copying from {source_path} to {destination_path}")
    
    return True