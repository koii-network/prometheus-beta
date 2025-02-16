import os

def is_file_read_only(file_path):
    """
    Determine if a file is read-only.
    
    Args:
        file_path (str): Path to the file to check.
    
    Returns:
        bool: True if the file is read-only, False otherwise.
    
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    # Validate file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file permissions using os.access() with os.R_OK
    is_readable = os.access(file_path, os.R_OK)
    
    # Check if the file has write permissions
    is_writable = os.access(file_path, os.W_OK)
    
    # File is read-only if it's readable but not writable
    return is_readable and not is_writable