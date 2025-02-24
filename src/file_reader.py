"""
Module for reading text file contents.

This module provides a function to read the contents of a text file
with error handling for common file-related issues.
"""

def read_text_file(file_path):
    """
    Read and return the contents of a text file.

    Args:
        file_path (str): The path to the text file to be read.

    Returns:
        str: The contents of the text file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to read the file.
        IsADirectoryError: If the path is a directory instead of a file.
        IOError: For other input/output related errors.
    """
    # Validate input is a non-empty string
    if not isinstance(file_path, str) or not file_path:
        raise ValueError("File path must be a non-empty string")

    # Open the file, read contents, and automatically close the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read '{file_path}'.")
    except IsADirectoryError:
        raise IsADirectoryError(f"'{file_path}' is a directory, not a file.")
    except IOError as e:
        raise IOError(f"Error reading file '{file_path}': {str(e)}")