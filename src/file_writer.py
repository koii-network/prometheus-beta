"""
Module for writing strings to text files.
"""

def write_string_to_file(file_path: str, content: str, mode: str = 'w') -> None:
    """
    Write a string to a text file.

    Args:
        file_path (str): The path to the file where the string will be written.
        content (str): The string content to write to the file.
        mode (str, optional): The file writing mode. Defaults to 'w' (write).
            Use 'a' for append mode.

    Raises:
        TypeError: If file_path or content is not a string.
        ValueError: If file_path is an empty string.
        PermissionError: If the file cannot be written due to permissions.
        IOError: If there are issues writing to the file.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(content, str):
        raise TypeError("content must be a string")
    
    # Validate file path
    if not file_path:
        raise ValueError("file_path cannot be an empty string")
    
    # Write to file
    try:
        with open(file_path, mode, encoding='utf-8') as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to write to {file_path}")
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {e}")