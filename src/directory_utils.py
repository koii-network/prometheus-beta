import os
import shutil

def delete_directory(path):
    """
    Recursively delete a directory and all its contents.

    Args:
        path (str): Path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the specified path does not exist.
        PermissionError: If the user lacks permission to delete the directory.
        ValueError: If the path is not a directory.
    """
    # Normalize the path to handle different path formats
    full_path = os.path.abspath(os.path.expanduser(path))

    # Validate input
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"The path {full_path} does not exist.")
    
    if not os.path.isdir(full_path):
        raise ValueError(f"The path {full_path} is not a directory.")

    # Use shutil.rmtree for recursive deletion
    try:
        shutil.rmtree(full_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete {full_path}")
    except Exception as e:
        raise RuntimeError(f"Error deleting directory: {e}")