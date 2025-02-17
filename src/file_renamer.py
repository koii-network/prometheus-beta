import os
import shutil

def rename_file(source_path, destination_path):
    """
    Rename a file from source path to destination path.
    
    Args:
        source_path (str): The current path of the file to be renamed.
        destination_path (str): The new path for the file.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are permission issues.
        IsADirectoryError: If the source is a directory.
        FileExistsError: If the destination file already exists.
    
    Returns:
        str: The new path of the renamed file.
    """
    # Validate source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Prevent renaming directories
    if os.path.isdir(source_path):
        raise IsADirectoryError(f"Cannot rename a directory: {source_path}")
    
    # Check if destination already exists
    if os.path.exists(destination_path):
        raise FileExistsError(f"Destination file already exists: {destination_path}")
    
    try:
        # Ensure destination directory exists
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        
        # Rename the file
        shutil.move(source_path, destination_path)
        
        return destination_path
    except PermissionError:
        raise PermissionError(f"Permission denied when renaming {source_path} to {destination_path}")