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
        IsADirectoryError: If the source path is a directory instead of a file.
        PermissionError: If there are insufficient permissions to read source or write destination.
        ValueError: If source and destination paths are the same.
    
    Returns:
        str: The absolute path of the newly copied file.
    """
    # Normalize paths to handle relative paths
    source_path = os.path.abspath(os.path.normpath(source_path))
    destination_path = os.path.abspath(os.path.normpath(destination_path))
    
    # Check if source and destination are the same
    if source_path == destination_path:
        raise ValueError("Source and destination paths cannot be the same.")
    
    # Validate source file exists and is a file
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path is not a file: {source_path}")
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Perform the file copy
    try:
        shutil.copy2(source_path, destination_path)
        return destination_path
    except PermissionError:
        raise PermissionError(f"Permission denied when copying from {source_path} to {destination_path}")