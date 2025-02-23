import os
import shutil


def copy_file(source_path, destination_path):
    """
    Copy a file from source location to destination location.

    Args:
        source_path (str): Path to the source file to be copied.
        destination_path (str): Path where the file should be copied to.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to read/write.
        IsADirectoryError: If source is a directory instead of a file.
        ValueError: If source and destination paths are the same.

    Returns:
        str: The path of the newly copied file.
    """
    # Validate input paths
    if not isinstance(source_path, str) or not isinstance(destination_path, str):
        raise TypeError("Paths must be strings")

    # Normalize paths to resolve any relative path issues
    source_path = os.path.abspath(os.path.normpath(source_path))
    destination_path = os.path.abspath(os.path.normpath(destination_path))

    # Check if source and destination are the same
    if source_path == destination_path:
        raise ValueError("Source and destination paths cannot be the same")

    # Ensure source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")

    # Ensure source is a file, not a directory
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path is not a file: {source_path}")

    # Ensure destination directory exists, create if not
    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Perform the file copy
    try:
        shutil.copy2(source_path, destination_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot copy to {destination_path}")

    return destination_path