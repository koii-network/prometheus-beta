import os

def is_hidden_file(file_path):
    """
    Determine if a file is hidden.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is hidden, False otherwise.

    Raises:
        TypeError: If file_path is not a string.
        FileNotFoundError: If the file does not exist.
    """
    # Type checking
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    # Expand user and get absolute path
    full_path = os.path.abspath(os.path.expanduser(file_path))

    # Check if file exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File not found: {full_path}")

    # Get the filename
    filename = os.path.basename(full_path)

    # On Unix-like systems (Linux, macOS), hidden files start with a dot
    if filename.startswith('.'):
        return True

    # On Windows, use file attributes
    if os.name == 'nt':
        try:
            # Use Windows-specific file attribute check
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x2
            attributes = ctypes.windll.kernel32.GetFileAttributesW(full_path)
            return bool(attributes & FILE_ATTRIBUTE_HIDDEN)
        except (ImportError, AttributeError):
            # Fallback to filename check if ctypes method fails
            return filename.startswith('.')

    return False