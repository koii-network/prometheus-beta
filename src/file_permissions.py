import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.
    
    Args:
        file_path (str): Path to the file whose permissions will be changed.
        mode (int): Octal representation of the new file permissions (e.g., 0o755).
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permission to change file permissions.
        TypeError: If invalid arguments are provided.
    
    Returns:
        bool: True if permissions were successfully changed.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer (octal representation)")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    try:
        # Change file permissions
        os.chmod(file_path, mode)
        return True
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to change {file_path}'s mode")