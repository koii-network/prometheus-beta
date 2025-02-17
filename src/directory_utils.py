import os
import shutil

def delete_directory(path):
    """
    Delete a directory and all its contents.
    
    Args:
        path (str): Path to the directory to be deleted.
    
    Raises:
        FileNotFoundError: If the directory does not exist.
        PermissionError: If there are permission issues deleting the directory.
        ValueError: If the path is not a directory.
    """
    # Normalize the path to remove any trailing slashes
    path = os.path.normpath(path)
    
    # Check if path exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")
    
    # Check if path is a directory
    if not os.path.isdir(path):
        raise ValueError(f"Path is not a directory: {path}")
    
    try:
        # Use shutil.rmtree to recursively delete the directory and its contents
        shutil.rmtree(path)
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to delete directory: {path}")