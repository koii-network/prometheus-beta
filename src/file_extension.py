"""
Module for extracting file extensions from file paths.
"""

import os


def get_file_extension(file_path):
    """
    Extract the file extension from a given file path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The file extension (without the dot), or an empty string if no extension exists.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(file_path, str):
        raise TypeError("Input must be a string")
    
    # Use os.path.splitext to extract the extension
    filename = os.path.basename(file_path)
    _, extension = os.path.splitext(filename)
    
    # Remove the leading dot and return the extension (or empty string)
    return extension.lstrip('.')