import os
import stat

def is_file_read_only(file_path):
    """
    Determine if a file is read-only.

    Args:
        file_path (str): Path to the file to check.

    Returns:
        bool: True if the file is read-only, False otherwise.

    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If file_path is not a string.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Get file mode and check write permissions
    file_mode = os.stat(file_path).st_mode
    return not bool(file_mode & stat.S_IWUSR)