import os
import shutil

def copy_file(source_path, destination_path):
    """
    Copy a file from source location to destination location.
    
    Args:
        source_path (str): Path to the source file to be copied.
        destination_path (str): Path where the file should be copied to.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        IsADirectoryError: If source path is a directory instead of a file.
        PermissionError: If there are insufficient permissions to copy the file.
    
    Returns:
        str: The path of the newly copied file.
    """
    # Validate source file exists and is a file
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path is not a file: {source_path}")
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Copy the file
    try:
        shutil.copy2(source_path, destination_path)
        return destination_path
    except PermissionError:
        raise PermissionError(f"Permission denied when copying file from {source_path} to {destination_path}")