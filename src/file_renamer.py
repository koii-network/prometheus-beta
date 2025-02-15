import os
import shutil

def rename_file(source_path, destination_path):
    """
    Rename a file from source path to destination path.
    
    Args:
        source_path (str): The current path of the file to be renamed.
        destination_path (str): The new path and name for the file.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to rename the file.
        IsADirectoryError: If the source path is a directory instead of a file.
    """
    # Validate input paths
    if not isinstance(source_path, str) or not isinstance(destination_path, str):
        raise TypeError("Paths must be strings")
    
    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Check if source is a file (not a directory)
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path is not a file: {source_path}")
    
    try:
        # Ensure the destination directory exists
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        
        # Rename/move the file
        shutil.move(source_path, destination_path)
        return True
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot rename {source_path}")
    except Exception as e:
        raise RuntimeError(f"Error renaming file: {e}")