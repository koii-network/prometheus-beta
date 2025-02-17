import os
import stat

def change_file_permissions(file_path, mode):
    """
    Change the permissions of a file.

    Args:
        file_path (str): Path to the file whose permissions are to be changed.
        mode (int): New permissions mode (in octal, e.g., 0o755 for rwxr-xr-x).

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user lacks permissions to change the file mode.
        TypeError: If file_path is not a string or mode is not an integer.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(mode, int):
        raise TypeError("mode must be an integer (octal)")

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Change file permissions
        os.chmod(file_path, mode)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot change mode of {file_path}")