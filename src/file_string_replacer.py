"""
Module for replacing strings in files.
"""

def replace_string_in_file(file_path, old_string, new_string):
    """
    Replace all occurrences of a given string in a file.

    Args:
        file_path (str): Path to the file to be modified.
        old_string (str): The string to be replaced.
        new_string (str): The string to replace with.

    Returns:
        int: Number of replacements made.

    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If any of the arguments are not strings.
        ValueError: If old_string is an empty string.
    """
    # Validate input types
    if not all(isinstance(arg, str) for arg in [file_path, old_string, new_string]):
        raise TypeError("All arguments must be strings")
    
    # Validate old_string is not empty
    if not old_string:
        raise ValueError("Old string cannot be empty")
    
    # Read the file contents
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Count the number of replacements
    replacements_count = file_contents.count(old_string)
    
    # Replace the string
    modified_contents = file_contents.replace(old_string, new_string)
    
    # Write the modified contents back to the file
    with open(file_path, 'w') as file:
        file.write(modified_contents)
    
    return replacements_count