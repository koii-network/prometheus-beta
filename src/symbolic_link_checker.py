import os

def is_symbolic_link(file_path):
    """
    Detect whether a given file path is a symbolic link.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is a symbolic link, False otherwise.

    Raises:
        TypeError: If the input is not a string.
        FileNotFoundError: If the file path does not exist.
    """
    # Check if input is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Use os.path.islink to check if it's a symbolic link
    return os.path.islink(file_path)