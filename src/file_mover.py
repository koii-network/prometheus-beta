import os
import shutil

def move_file(source_path, destination_path):
    """
    Move a file from the source path to the destination path.

    Args:
        source_path (str): The current path of the file to be moved.
        destination_path (str): The target path where the file should be moved.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to move the file.
        IsADirectoryError: If the source path is a directory instead of a file.
        ValueError: If source or destination paths are invalid or empty.
    """
    # Validate input paths
    if not source_path or not destination_path:
        raise ValueError("Source and destination paths must not be empty")

    # Normalize paths to handle potential relative path issues
    source_path = os.path.abspath(os.path.normpath(source_path))
    destination_path = os.path.abspath(os.path.normpath(destination_path))

    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")

    # Ensure source is a file, not a directory
    if os.path.isdir(source_path):
        raise IsADirectoryError(f"Source path is a directory, not a file: {source_path}")

    # Ensure destination directory exists, create if not
    destination_dir = os.path.dirname(destination_path)
    os.makedirs(destination_dir, exist_ok=True)

    try:
        # Move the file
        shutil.move(source_path, destination_path)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to move file from {source_path} to {destination_path}")
    
    return destination_path  # Return the new file path for confirmation