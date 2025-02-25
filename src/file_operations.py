import os
import pathlib

def delete_file(file_path):
    """
    Delete a file from the given path.

    Args:
        file_path (str or pathlib.Path): Path to the file to be deleted.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user lacks permission to delete the file.
        IsADirectoryError: If the path is a directory instead of a file.
        ValueError: If the file path is invalid or empty.

    Returns:
        bool: True if the file was successfully deleted.
    """
    # Convert to Path object if string is provided
    path = pathlib.Path(file_path)

    # Validate input
    if not path:
        raise ValueError("File path cannot be empty or None")

    # Check if path exists
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    # Check if it's a file (not a directory)
    if not path.is_file():
        raise IsADirectoryError(f"Path is a directory, not a file: {path}")

    # Delete the file
    try:
        path.unlink()
        return True
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete file {path}")