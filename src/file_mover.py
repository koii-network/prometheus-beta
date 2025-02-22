import os
import shutil

def move_file(source_path, destination_path):
    """
    Move a file from source path to destination path.
    
    Args:
        source_path (str): The relative path of the source file to move.
        destination_path (str): The relative path where the file should be moved.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        IsADirectoryError: If the source path is a directory instead of a file.
        PermissionError: If there are insufficient permissions to move the file.
    
    Returns:
        str: The new path of the moved file.
    """
    # Normalize paths to handle relative paths correctly
    source_path = os.path.normpath(source_path)
    destination_path = os.path.normpath(destination_path)
    
    # Ensure source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Ensure source is a file, not a directory
    if os.path.isdir(source_path):
        raise IsADirectoryError(f"Source path is a directory, not a file: {source_path}")
    
    # Ensure destination directory exists, create if it doesn't
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    try:
        # Move the file
        shutil.move(source_path, destination_path)
        return destination_path
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to move file from {source_path} to {destination_path}")