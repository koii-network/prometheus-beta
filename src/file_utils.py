import os
from datetime import datetime

def get_last_modified_date(file_path):
    """
    Get the last modified date of a file.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        datetime: The last modified datetime of the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If there's an error accessing the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        # Get last modified timestamp
        mtime = os.path.getmtime(file_path)
        # Convert timestamp to datetime
        return datetime.fromtimestamp(mtime)
    except OSError as e:
        raise OSError(f"Error accessing file {file_path}: {e}")