import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.
    
    Args:
        file_path (str): Path to the file whose permissions are to be changed.
        mode (int): New file permissions in octal format (e.g., 0o755).
    
    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If the mode is not an integer.
        ValueError: If the mode is not a valid permission value.
    """
    # Validate inputs
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("Mode must be an integer")
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate mode is an octal permission value
    if mode < 0 or mode > 0o777:
        raise ValueError("Invalid permission mode. Must be between 0 and 0o777")
    
    # Change file permissions
    try:
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Permission denied: Unable to change permissions of {file_path}")
    
    return True