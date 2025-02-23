import os
import getpass
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file by its path.

    Args:
        file_path (str): Path to the file whose owner is to be retrieved.

    Returns:
        str: The username of the file's owner.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there's insufficient permission to get file stats.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Expand any user path (like ~) and get absolute path
    file_path = os.path.abspath(os.path.expanduser(file_path))
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Get file stats and retrieve owner
        file_stat = os.stat(file_path)
        owner_uid = file_stat.st_uid
        
        # Convert UID to username
        try:
            return pwd.getpwuid(owner_uid).pw_name
        except KeyError:
            # Fallback: return UID as string if username lookup fails
            return str(owner_uid)
    
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to get owner of {file_path}")