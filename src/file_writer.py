def write_string_to_file(file_path, content):
    """
    Write a given string to a text file.
    
    Args:
        file_path (str): The path to the file where the content will be written.
        content (str): The string content to write to the file.
    
    Raises:
        TypeError: If file_path or content is not a string.
        IOError: If there's an error writing to the file.
    """
    # Validate input types
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    if not isinstance(content, str):
        raise TypeError("content must be a string")
    
    try:
        # Open the file in write mode, which will create the file if it doesn't exist
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        # Raise an IOError if there's a problem writing to the file
        raise IOError(f"Error writing to file {file_path}: {e}")