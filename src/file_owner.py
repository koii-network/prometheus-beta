import os
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: The username of the file owner.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If there's an error retrieving file ownership.
    """
    # Expand any user shortcuts and get absolute path
    full_path = os.path.abspath(os.path.expanduser(file_path))
    
    # Check if file exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File not found: {full_path}")
    
    try:
        # Get file stats
        file_stat = os.stat(full_path)
        
        # Get owner username from user ID
        return pwd.getpwuid(file_stat.st_uid).pw_name
    
    except Exception as e:
        raise OSError(f"Could not retrieve file owner: {str(e)}")