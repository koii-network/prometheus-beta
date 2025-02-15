def write_string_to_file(file_path, content):
    """
    Write a string to a text file.
    
    Args:
        file_path (str): Path to the file where the content will be written.
        content (str): The string content to write to the file.
    
    Raises:
        TypeError: If content is not a string.
        IOError: If there's an issue writing to the file.
    """
    # Validate input is a string
    if not isinstance(content, str):
        raise TypeError("Content must be a string")
    
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {e}")