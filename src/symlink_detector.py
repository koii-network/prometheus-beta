import os

def is_symbolic_link(file_path: str) -> bool:
    """
    Detect whether a given file path is a symbolic link.
    
    Args:
        file_path (str): The path to the file to check
    
    Returns:
        bool: True if the file is a symbolic link, False otherwise
    
    Raises:
        FileNotFoundError: If the file or path does not exist
    """
    # Validate input
    if not file_path or not isinstance(file_path, str):
        raise ValueError("File path must be a non-empty string")
    
    # Expand user and resolve absolute path
    abs_path = os.path.abspath(os.path.expanduser(file_path))
    
    # Check if path exists first
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"Path does not exist: {abs_path}")
    
    # Use os.path.islink() to check if it's a symbolic link
    return os.path.islink(abs_path)