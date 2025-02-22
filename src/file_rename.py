import os
import shutil

def rename_file(source_path, destination_path):
    """
    Rename or move a file from source path to destination path.
    
    Args:
        source_path (str): The current path of the file to be renamed/moved
        destination_path (str): The new path for the file
    
    Raises:
        FileNotFoundError: If the source file does not exist
        PermissionError: If there are insufficient permissions to rename/move the file
        IsADirectoryError: If source_path is a directory instead of a file
    
    Returns:
        str: The new path of the renamed/moved file
    """
    # Validate source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Ensure source is a file, not a directory
    if os.path.isdir(source_path):
        raise IsADirectoryError(f"Source path is a directory, not a file: {source_path}")
    
    # Ensure destination directory exists
    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Perform the rename/move operation
    try:
        shutil.move(source_path, destination_path)
        return destination_path
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot rename/move {source_path} to {destination_path}")