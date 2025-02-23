"""
Module for appending text to existing files.

This module provides a function to safely append text to an existing file,
with error handling for various potential issues.
"""

import os


def append_text_to_file(file_path: str, text: str) -> None:
    """
    Append text to an existing file.

    Args:
        file_path (str): The path to the file to append text to.
        text (str): The text to append to the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to write to the file.
        TypeError: If file_path or text is not a string.
        ValueError: If file_path is an empty string.

    Example:
        >>> append_text_to_file('example.txt', 'New line of text')
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Validate file_path is not empty
    if not file_path.strip():
        raise ValueError("file_path cannot be an empty string")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    # Check if path is a directory
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"{file_path} is a directory, not a file")
    
    # Append text to the file
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(text)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot write to {file_path}")