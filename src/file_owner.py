import os
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file by its username.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        str: Username of the file owner
    
    Raises:
        FileNotFoundError: If the file does not exist
        OSError: If there's an error retrieving file information
    """
    # Verify file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Get file stats
        file_stat = os.stat(file_path)
        
        # Convert UID to username
        owner = pwd.getpwuid(file_stat.st_uid).pw_name
        
        return owner
    
    except (FileNotFoundError, OSError) as e:
        raise OSError(f"Could not retrieve file owner: {e}")