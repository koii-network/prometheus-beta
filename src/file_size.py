import os

def get_file_size(file_path):
    """
    Get the size of a file in bytes.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        int: Size of the file in bytes.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be accessed.
        IsADirectoryError: If the path is a directory.
    """
    # Normalize the file path to handle different path representations
    normalized_path = os.path.normpath(file_path)

    # Check if file exists and is a file (not a directory)
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"File not found: {normalized_path}")
    
    if os.path.isdir(normalized_path):
        raise IsADirectoryError(f"Path is a directory, not a file: {normalized_path}")

    # Get and return file size
    return os.path.getsize(normalized_path)