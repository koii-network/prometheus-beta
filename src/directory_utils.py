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

    # Attempt to change permissions to allow deletion
    try:
        # Change permissions to allow writing
        os.chmod(full_path, 0o755)
        
        # Recursively change permissions of all contents
        for root, dirs, files in os.walk(full_path):
            for dir_name in dirs:
                os.chmod(os.path.join(root, dir_name), 0o755)
            for file_name in files:
                os.chmod(os.path.join(root, file_name), 0o644)
    except PermissionError:
        raise PermissionError(f"Cannot modify permissions of {full_path}")

    # Use shutil.rmtree for recursive deletion
    try:
        shutil.rmtree(full_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete {full_path}")
    except Exception as e:
        raise RuntimeError(f"Error deleting directory: {e}")