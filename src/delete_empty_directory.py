import os
import shutil

def delete_empty_directory(directory_path):
    """
    Delete an empty directory.

    Args:
        directory_path (str): Path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the directory does not exist.
        OSError: If the directory is not empty or cannot be deleted.
        ValueError: If the directory_path is None or an empty string.

    Returns:
        bool: True if the directory was successfully deleted.
    """
    # Validate input
    if not directory_path:
        raise ValueError("Directory path cannot be None or empty")

    # Normalize the path to handle different path formats
    directory_path = os.path.normpath(directory_path)

    # Check if directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    # Check if it's actually a directory
    if not os.path.isdir(directory_path):
        raise OSError(f"Path is not a directory: {directory_path}")

    # Check if directory is empty
    if os.listdir(directory_path):
        raise OSError(f"Directory is not empty: {directory_path}")

    try:
        # Remove the directory
        os.rmdir(directory_path)
        return True
    except PermissionError:
        raise OSError(f"Permission denied: Cannot delete directory {directory_path}")