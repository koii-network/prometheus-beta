import os
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file by its path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The username of the file's owner.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access file metadata.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Get file stats
        file_stats = os.stat(file_path)
        
        # Get owner username from the user ID
        owner = pwd.getpwuid(file_stats.st_uid).pw_name
        return owner
    except PermissionError:
        raise PermissionError(f"Cannot access metadata for file: {file_path}")