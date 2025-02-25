"""
Module for replacing strings in files.

This module provides a function to replace all occurrences of a specific 
string with another string in a given file.
"""

def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a string in a file.

    Args:
        file_path (str): Path to the file to be modified.
        old_string (str): The string to be replaced.
        new_string (str): The string to replace with.

    Raises:
        ValueError: If any of the input arguments are invalid.
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to read/write the file.
        IOError: If there's an error reading or writing the file.

    Returns:
        bool: True if replacements were made, False if no replacements occurred.
    """
    # Validate input arguments
    if not isinstance(file_path, str) or not file_path:
        raise ValueError("File path must be a non-empty string")
    
    if not isinstance(old_string, str):
        raise ValueError("Old string must be a string")
    
    if new_string is None:
        raise ValueError("New string cannot be None")
    
    # Ensure new_string is converted to string
    new_string = str(new_string)

    # Read the file contents
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when reading file: {file_path}")
    except IOError as e:
        raise IOError(f"Error reading file: {e}")

    # Check if replacement is needed
    if old_string not in file_contents:
        return False

    # Replace all occurrences
    new_contents = file_contents.replace(old_string, new_string)

    # Write the modified contents back to the file
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_contents)
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to file: {file_path}")
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")

    return True