import os

def is_file_readonly(file_path):
    """
    Determine if a file is read-only.
    
    Args:
        file_path (str): Path to the file to check.
    
    Returns:
        bool: True if the file is read-only, False otherwise.
    
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file permissions
    return not os.access(file_path, os.W_OK)