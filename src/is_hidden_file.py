import os

def is_hidden_file(file_path):
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
    
    # Get the absolute path to handle relative paths
    abs_path = os.path.abspath(file_path)
    
    # Check if file exists
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Get the filename
    filename = os.path.basename(abs_path)
    
    # On Unix-like systems (Linux, macOS), hidden files start with a dot
    if filename.startswith('.'):
        return True
    
    # On Windows, use file attributes
    if os.name == 'nt':
        try:
            # Use Windows-specific file attribute check
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x02
            attributes = ctypes.windll.kernel32.GetFileAttributesW(abs_path)
            return bool(attributes & FILE_ATTRIBUTE_HIDDEN)
        except (ImportError, AttributeError):
            # Fallback to filename check on Windows
            return filename.startswith('.')
    
    return False