import os
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The username of the file owner.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there's no permission to access the file.
        OSError: For other OS-related errors when retrieving file owner.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Get file stats and retrieve owner
        file_stat = os.stat(file_path)
        return pwd.getpwuid(file_stat.st_uid).pw_name
    except PermissionError:
        raise PermissionError(f"Permission denied accessing file: {file_path}")
    except OSError as e:
        raise OSError(f"Error retrieving file owner: {e}")