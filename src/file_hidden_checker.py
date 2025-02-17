import os

def is_hidden_file(file_path):
    """
    Determine if a file is hidden based on its name or OS-specific attributes.
    
    Args:
        file_path (str): The path to the file to check.
    
    Returns:
        bool: True if the file is hidden, False otherwise.
    """
    # Check if the filename starts with a dot (Unix/Linux hidden file convention)
    filename = os.path.basename(file_path)
    if filename.startswith('.'):
        return True
    
    # On Windows, check file attributes
    if os.name == 'nt':
        import ctypes
        try:
            # Get file attributes
            attr = ctypes.windll.kernel32.GetFileAttributesW(file_path)
            return attr != -1 and bool(attr & 0x02)  # FILE_ATTRIBUTE_HIDDEN
        except Exception:
            return False
    
    return False