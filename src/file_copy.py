import shutil
import os

def copy_file(source_path, destination_path):
    """
    Copy a file from source location to destination location.

    Args:
        source_path (str): Path to the source file to be copied.
        destination_path (str): Path where the file should be copied to.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to read/write.
        IsADirectoryError: If source is a directory instead of a file.
        OSError: For other OS-related errors during file copy.

    Returns:
        bool: True if file was successfully copied, False otherwise.
    """
    # Validate input paths
    if not isinstance(source_path, str) or not isinstance(destination_path, str):
        raise TypeError("Paths must be strings")

    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")

    # Check if source is a file (not a directory)
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path is not a file: {source_path}")

    # Ensure destination directory exists
    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    try:
        # Use shutil for robust file copying
        shutil.copy2(source_path, destination_path)
        return True
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to copy from {source_path} to {destination_path}")
    except OSError as e:
        raise OSError(f"Error copying file: {e}")