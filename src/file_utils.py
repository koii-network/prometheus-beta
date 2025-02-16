import os
from datetime import datetime

def get_file_last_modified_date(file_path):
    """
    Get the last modified date of a file.
    
    Args:
        file_path (str): The relative path to the file.
    
    Returns:
        datetime: The last modified datetime of the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If there's an error accessing the file.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Resolve the absolute path to handle relative paths
    abs_path = os.path.abspath(file_path)
    
    # Check if file exists
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(abs_path):
        raise OSError(f"Path is not a file: {file_path}")
    
    # Get last modified timestamp and convert to datetime
    try:
        mtime = os.path.getmtime(abs_path)
        return datetime.fromtimestamp(mtime)
    except OSError as e:
        raise OSError(f"Error accessing file {file_path}: {str(e)}")