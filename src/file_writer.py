def write_string_to_file(file_path, content):
    """
    Write a given string to a text file.
    
    Args:
        file_path (str): The path to the file where the string will be written.
        content (str): The string content to write to the file.
    
    Raises:
        TypeError: If file_path or content is not a string.
        ValueError: If file_path is an empty string.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    if not isinstance(content, str):
        raise TypeError("content must be a string")
    
    # Validate file path is not empty
    if not file_path:
        raise ValueError("file_path cannot be an empty string")
    
    # Write the content to the file
    with open(file_path, 'w') as file:
        file.write(content)