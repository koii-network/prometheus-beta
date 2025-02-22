import os

def is_symlink(file_path):
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
    # Check input type
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Check file existence 
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Use os.path.islink() to detect symbolic links
    return os.path.islink(file_path)