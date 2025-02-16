import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.
    
    Args:
        file_path (str): The path to the file whose permissions will be changed.
        mode (int): The new permission mode (e.g., 0o755 for rwxr-xr-x).
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to change the file's mode.
        TypeError: If invalid arguments are provided.
    
    Returns:
        bool: True if permissions were successfully changed.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
        return True
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot change mode of {file_path}")