import os
from datetime import datetime

def get_file_last_modified_date(file_path):
    """
    Get the last modified date of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        datetime: The last modified date and time of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
        TypeError: If the file_path is not a string.
    """
    # Check if file_path is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    # Check if file exists and is accessible
    try:
        # Get the last modified timestamp
        modified_timestamp = os.path.getmtime(file_path)
        
        # Convert timestamp to datetime object
        return datetime.fromtimestamp(modified_timestamp)
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied accessing file: {file_path}")