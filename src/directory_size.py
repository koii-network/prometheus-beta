import os
import pathlib

def get_total_directory_size(directory_path):
    """
    Calculate the total size of all files in a given directory.

    Args:
        directory_path (str): Path to the directory to calculate file sizes.

    Returns:
        int: Total size of all files in bytes.

    Raises:
        TypeError: If directory_path is not a string.
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the path is not a directory.
    """
    # Validate input type
    if not isinstance(directory_path, str):
        raise TypeError("Directory path must be a string")

    # Convert to absolute path and validate directory
    dir_path = pathlib.Path(directory_path).resolve()

    # Check if directory exists
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    # Check if it's a directory
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")

    # Calculate total size
    total_size = 0
    for entry in dir_path.rglob('*'):
        if entry.is_file():
            try:
                total_size += entry.stat().st_size
            except (PermissionError, OSError):
                # Skip files that can't be accessed
                continue

    return total_size