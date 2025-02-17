import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.
    
    Args:
        file_path (str): Path to the file whose permissions are to be changed.
        mode (int): Octal representation of the new file permissions.
                    For example, 0o755 (owner can read/write/execute, 
                    group and others can read/execute)
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to change file permissions.
        TypeError: If the mode is not an integer.
        ValueError: If the mode is not a valid permission value.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer")
    
    # Check file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate mode is an octal permission value
    if mode < 0 or mode > 0o777:
        raise ValueError("Invalid file permission mode. Must be between 0 and 0o777")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to change mode of {file_path}")
    
    return True