import os
import shutil

def delete_directory(path):
    """
    Delete a directory and all its contents.
    
    Args:
        path (str): Path to the directory to be deleted.
    
    Raises:
        FileNotFoundError: If the directory does not exist.
        PermissionError: If there are permission issues.
        OSError: For other OS-related errors during deletion.
    """
    # Validate input
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    
    # Get absolute path to handle relative paths
    abs_path = os.path.abspath(path)
    
    # Check if directory exists
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"Directory not found: {path}")
    
    # Check if it's actually a directory
    if not os.path.isdir(abs_path):
        raise NotADirectoryError(f"Path is not a directory: {path}")
    
    try:
        # Use shutil.rmtree to remove directory and all its contents
        shutil.rmtree(abs_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to delete directory: {path}")
    except OSError as e:
        raise OSError(f"Error deleting directory {path}: {str(e)}")