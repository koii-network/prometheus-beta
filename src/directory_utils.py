import os
import shutil

def delete_directory(path):
    """
    Recursively delete a directory and all its contents.

    Args:
        path (str): The path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the user lacks permissions to delete the directory.
        ValueError: If the path is not a directory.
    """
    # Normalize the path to resolve any relative path components
    normalized_path = os.path.abspath(os.path.normpath(path))

    # Validate input
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"Directory not found: {normalized_path}")
    
    if not os.path.isdir(normalized_path):
        raise ValueError(f"Path is not a directory: {normalized_path}")

    try:
        # Use shutil.rmtree for recursive directory deletion
        shutil.rmtree(normalized_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete directory {normalized_path}")
    except Exception as e:
        raise RuntimeError(f"Error deleting directory: {e}")