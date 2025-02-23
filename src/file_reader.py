"""
Module for reading file contents with robust error handling.
"""

def read_file_contents(file_path):
    """
    Read and return the contents of a file.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        str: Contents of the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to read the file.
        IsADirectoryError: If the path is a directory instead of a file.
        IOError: For other I/O related errors.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read: {file_path}")
    except IsADirectoryError:
        raise IsADirectoryError(f"Path is a directory, not a file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {str(e)}")