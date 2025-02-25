import os

def get_file_size(file_path):
    """
    Get the size of a file in bytes.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        int: The size of the file in bytes.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
        IsADirectoryError: If the path is a directory instead of a file.
        TypeError: If the input is not a string.
    """
    # Validate input is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    # Explicitly check if path is a directory before attempting to get size
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"Path is a directory, not a file: {file_path}")

    # Use os.path.getsize to get file size
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"No file found at path: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied accessing file: {file_path}")