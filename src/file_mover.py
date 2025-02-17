import os
import shutil

def move_file(source_path, destination_path):
    """
    Move a file from the source path to the destination path.
    
    Args:
        source_path (str): Relative path of the source file to move
        destination_path (str): Relative path where the file should be moved
    
    Raises:
        FileNotFoundError: If the source file does not exist
        IsADirectoryError: If the source path is a directory instead of a file
        PermissionError: If there are insufficient permissions to move the file
    """
    # Ensure absolute paths are converted to paths relative to the current working directory
    source_path = os.path.normpath(source_path)
    destination_path = os.path.normpath(destination_path)
    
    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file {source_path} does not exist")
    
    # Check if source is a file, not a directory
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path {source_path} is not a file")
    
    # Ensure destination directory exists, create if it doesn't
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Move the file
    shutil.move(source_path, destination_path)
    
    return True