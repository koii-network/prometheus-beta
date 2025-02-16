import os

def is_hidden_file(filepath):
    """
    Determine if a file is hidden.
    
    A file is considered hidden if:
    1. Its filename starts with a dot (.) on Unix-like systems
    2. It has the hidden file attribute on Windows systems
    
    Args:
        filepath (str): Path to the file
    
    Returns:
        bool: True if the file is hidden, False otherwise
    """
    # Get the filename (last part of the path)
    filename = os.path.basename(filepath)
    
    # Check if filename starts with a dot (Unix-like hidden files)
    if filename.startswith('.'):
        return True
    
    # For Windows, check the hidden file attribute 
    # Note: This requires additional import on Windows
    if os.name == 'nt':
        try:
            import winreg
            attrs = os.getattr(filepath, 'FILE_ATTRIBUTE_HIDDEN')
            return bool(attrs & 0x2)
        except (ImportError, AttributeError):
            return False
    
    return False