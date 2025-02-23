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
        str: The file extension (including the dot) or an empty string if no extension exists.

    Examples:
        >>> get_file_extension('document.txt')
        '.txt'
        >>> get_file_extension('image.jpg')
        '.jpg'
        >>> get_file_extension('no_extension_file')
        ''
        >>> get_file_extension('/path/to/another.file.with.dots.py')
        '.py'
    """
    # Use os.path.splitext to handle various file path scenarios
    _, extension = os.path.splitext(file_path)
    return extension