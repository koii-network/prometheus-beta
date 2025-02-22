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
    # Validate the path 
    path = os.path.abspath(path)
    
    # Check if path exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")
    
    # Check if it's a directory
    if not os.path.isdir(path):
        raise ValueError(f"Path is not a directory: {path}")
    
    try:
        # Use shutil.rmtree to remove directory and all its contents
        shutil.rmtree(path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Unable to delete directory {path}")
    except Exception as e:
        raise OSError(f"Error deleting directory {path}: {str(e)}")