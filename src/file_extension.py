"""
Utility function to extract file extension from a given file path.
"""

import os


def get_file_extension(file_path: str) -> str:
    """
    Extract the file extension from a given file path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The file extension in lowercase, without the dot. 
             Returns an empty string if no extension is found.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(file_path, str):
        raise TypeError("Input must be a string")

    # Use os.path.splitext to separate the extension
    _, extension = os.path.splitext(file_path)

    # Remove the dot and convert to lowercase
    return extension.lstrip('.').lower()