import os

def is_file_hidden(file_path):
    """
    Determine if a file is hidden.
    
    Args:
        file_path (str): Path to the file to check.
    
    Returns:
        bool: True if the file is hidden, False otherwise.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If file_path is not a string.
    """
    # Check input type
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    # Check file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Get the filename
    filename = os.path.basename(file_path)
    
    # On Unix-like systems (Linux, macOS), hidden files start with a dot
    if filename.startswith('.'):
        return True
    
    # On Windows, use file attributes
    if os.name == 'nt':
        try:
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x2
            attributes = ctypes.windll.kernel32.GetFileAttributesW(file_path)
            return bool(attributes & FILE_ATTRIBUTE_HIDDEN)
        except (ImportError, AttributeError):
            # Fallback to filename check if Windows-specific method fails
            return filename.startswith('.')
    
    return False