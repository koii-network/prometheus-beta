import os
import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        datetime.datetime: The creation time of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If there's an error accessing file metadata.
    """
    # Expand user and normalize the path
    full_path = os.path.expanduser(file_path)

    # Check if file exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Use platform-specific methods to get creation time
        if os.name == 'nt':  # Windows
            creation_time = os.path.getctime(full_path)
        else:  # Unix-like systems (macOS, Linux)
            # Use stat for Unix-like systems
            stat = os.stat(full_path)
            # Try to get creation time, fall back to metadata change time if not available
            creation_time = getattr(stat, 'st_birthtime', stat.st_mtime)

        # Convert to datetime object
        return datetime.datetime.fromtimestamp(creation_time)

    except Exception as e:
        raise OSError(f"Error accessing file metadata: {str(e)}")