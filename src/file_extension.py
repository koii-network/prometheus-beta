import os

def get_file_extension(file_path):
    """
    Get the file extension from a given file path.
    
    Args:
        file_path (str): The path to the file.
    
    Returns:
        str: The file extension (without the dot) or an empty string if no extension.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Use os.path.splitext to separate the base and extension
    _, extension = os.path.splitext(file_path)
    
    # Remove the dot and return the extension (or empty string)
    return extension.lstrip('.')