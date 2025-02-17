def write_string_to_file(file_path, content):
    """
    Write a string to a specified file.
    
    Args:
        file_path (str): The path to the file where the content will be written.
        content (str): The string content to write to the file.
    
    Raises:
        TypeError: If file_path or content is not a string.
        ValueError: If file_path is an empty string.
    """
    # Validate input types
    if not isinstance(file_path, str) or not isinstance(content, str):
        raise TypeError("Both file_path and content must be strings")
    
    # Validate file path is not empty
    if not file_path:
        raise ValueError("File path cannot be an empty string")
    
    # Write content to the file
    with open(file_path, 'w') as file:
        file.write(content)