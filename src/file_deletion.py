import os


def delete_file(file_path):
    """
    Delete a file from the given file path.

    Args:
        file_path (str): The path to the file to be deleted.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user lacks permission to delete the file.
        IsADirectoryError: If the path is a directory instead of a file.
        TypeError: If the file_path is not a string.

    Returns:
        bool: True if the file was successfully deleted.
    """
    # Validate input type
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    # Expand the path to handle relative paths
    full_path = os.path.abspath(os.path.expanduser(file_path))

    # Check if the path exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")

    # Ensure it's a file, not a directory
    if os.path.isdir(full_path):
        raise IsADirectoryError(f"The path {file_path} is a directory, not a file")

    # Delete the file
    try:
        os.remove(full_path)
        return True
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete {file_path}")