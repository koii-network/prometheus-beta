import os
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Username of the file owner.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If there's an error retrieving file ownership.
    """
    # Validate file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Get file's stat information
        file_stat = os.stat(file_path)
        
        # Get username from the user ID
        owner = pwd.getpwuid(file_stat.st_uid).pw_name
        
        return owner
    except Exception as e:
        raise OSError(f"Could not retrieve file owner: {str(e)}")