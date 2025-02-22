import os

def is_hidden_file(file_path):
    """
    Determine if a file is hidden.
    
    A file is considered hidden if:
    1. Its filename starts with a dot (.) on Unix-like systems
    2. It has the hidden file attribute on Windows systems
    
    Args:
        file_path (str): Path to the file to check
    
    Returns:
        bool: True if the file is hidden, False otherwise
    
    Raises:
        FileNotFoundError: If the file does not exist
        TypeError: If file_path is not a string
    """
    # Check input type
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    # Check file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Get the filename (basename)
    filename = os.path.basename(file_path)
    
    # Check if filename starts with a dot (Unix-like hidden file)
    if filename.startswith('.'):
        return True
    
    # For Windows, check hidden file attribute 
    try:
        import ctypes
        FILE_ATTRIBUTE_HIDDEN = 0x02
        attributes = ctypes.windll.kernel32.GetFileAttributesW(file_path)
        return bool(attributes & FILE_ATTRIBUTE_HIDDEN)
    except (ImportError, AttributeError):
        # Fallback for non-Windows systems
        return False