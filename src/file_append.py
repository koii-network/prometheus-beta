def append_to_file(file_path, text):
    """
    Append text to an existing file.

    Args:
        file_path (str): The path to the file to append to.
        text (str): The text to append to the file.

    Raises:
        TypeError: If file_path or text is not a string.
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to write to the file.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Open file in append mode
    try:
        with open(file_path, 'a') as file:
            file.write(text)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist")
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to write to {file_path}")