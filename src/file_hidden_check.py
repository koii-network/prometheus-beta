import os

def is_hidden_file(file_path):
    """
    Determine if a file is hidden.

    Args:
        file_path (str): Path to the file to check for hidden status.

    Returns:
        bool: True if the file is hidden, False otherwise.

    Raises:
        TypeError: If file_path is not a string.
        FileNotFoundError: If the file does not exist.
    """
    # Check input type
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    # Expand user and get absolute path
    full_path = os.path.abspath(os.path.expanduser(file_path))

    # Check if file exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File not found: {full_path}")

    # Get filename
    filename = os.path.basename(full_path)

    # Check if file starts with a dot (Unix-like hidden file)
    if filename.startswith('.'):
        return True

    # Check Windows hidden file attribute (for Windows systems)
    try:
        import winreg
        if os.name == 'nt':
            attributes = os.stat(full_path).st_file_attributes
            return attributes & 2 != 0  # FILE_ATTRIBUTE_HIDDEN
    except (ImportError, AttributeError):
        pass

    return False