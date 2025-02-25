"""
Module for writing strings to files with robust error handling.
"""

import os
from typing import Union, Optional


def write_string_to_file(file_path: str, content: str, encoding: str = 'utf-8', 
                          overwrite: bool = False) -> None:
    """
    Write a string to a file with comprehensive error handling.

    Args:
        file_path (str): The path to the file where the string will be written.
        content (str): The string content to write to the file.
        encoding (str, optional): The text encoding to use. Defaults to 'utf-8'.
        overwrite (bool, optional): Whether to overwrite existing file. Defaults to False.

    Raises:
        ValueError: If content is not a string or file_path is empty.
        IOError: If there are issues writing to the file.
        PermissionError: If there are insufficient permissions to write the file.
    """
    # Validate inputs
    if not isinstance(content, str):
        raise ValueError("Content must be a string.")
    
    if not file_path or not isinstance(file_path, str):
        raise ValueError("File path must be a non-empty string.")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
    
    # Determine write mode based on overwrite flag
    write_mode = 'w' if overwrite else 'x'
    
    try:
        with open(file_path, write_mode, encoding=encoding) as file:
            file.write(content)
    except FileExistsError:
        raise IOError(f"File {file_path} already exists. Use overwrite=True to replace.")
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to write to {file_path}")
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {str(e)}")