import os

def is_symlink(file_path):
    """
    Detect whether the given file path is a symbolic link.
    
    Args:
        file_path (str): Path to the file to check
    
    Returns:
        bool: True if the file is a symbolic link, False otherwise
    
    Raises:
        TypeError: If file_path is not a string
        FileNotFoundError: If the file path does not exist
    """
    # Check input type
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file or directory found at {file_path}")
    
    # Use os.path.islink() to detect symbolic links
    return os.path.islink(file_path)