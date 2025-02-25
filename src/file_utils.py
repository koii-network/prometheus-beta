import os
from datetime import datetime

def get_file_last_modified_date(file_path):
    """
    Get the last modified date of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        datetime: The last modified datetime of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
        TypeError: If the file_path is not a string.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Get last modified timestamp and convert to datetime
    try:
        modified_timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(modified_timestamp)
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {file_path}")