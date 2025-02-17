import os
import shutil

def move_file(source_path, destination_path):
    """
    Move a file from source path to destination path.
    
    Args:
        source_path (str): The relative path of the file to be moved.
        destination_path (str): The relative path where the file should be moved to.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        IsADirectoryError: If the source path is a directory.
        PermissionError: If there are insufficient permissions to move the file.
    """
    # Normalize paths to handle any potential '..' or '.' 
    source_path = os.path.normpath(source_path)
    destination_path = os.path.normpath(destination_path)
    
    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Check if source is a file, not a directory
    if os.path.isdir(source_path):
        raise IsADirectoryError(f"Source path is a directory, not a file: {source_path}")
    
    # Ensure destination directory exists
    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Move the file
    try:
        shutil.move(source_path, destination_path)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to move file from {source_path} to {destination_path}")
    
    return destination_path