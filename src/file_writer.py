def write_string_to_file(file_path, content):
    """
    Write a string to a text file.
    
    Args:
        file_path (str): The path to the file where the content will be written.
        content (str): The string content to write to the file.
    
    Raises:
        TypeError: If file_path or content is not a string.
        ValueError: If file_path is an empty string.
    """
    # Check input types
    if not isinstance(file_path, str) or not isinstance(content, str):
        raise TypeError("file_path and content must be strings")
    
    # Check for empty file path
    if not file_path:
        raise ValueError("file_path cannot be an empty string")
    
    # Write the content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)