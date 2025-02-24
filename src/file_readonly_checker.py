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
    # Check if file exists first
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check if file is read-only by attempting to open in write mode
    try:
        # Try to open the file in write mode
        with open(file_path, 'a') as f:
            pass
        return False
    except PermissionError:
        # If PermissionError is raised, the file is read-only
        return True