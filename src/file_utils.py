def append_text_to_file(file_path, text_to_append):
    """
    Append text to an existing file.
    
    Args:
        file_path (str): Path to the file where text will be appended
        text_to_append (str): Text to append to the file
    
    Raises:
        FileNotFoundError: If the specified file does not exist
        TypeError: If file_path or text_to_append is not a string
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(text_to_append, str):
        raise TypeError("text_to_append must be a string")
    
    # Check if file exists
    try:
        with open(file_path, 'a') as file:
            file.write(text_to_append)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist")