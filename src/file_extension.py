import os

def get_file_extension(file_path):
    """
    Get the file extension from a given file path.
    
    Args:
        file_path (str): The path to the file.
    
    Returns:
        str: The file extension (without the dot) or an empty string if no extension exists.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(file_path, str):
        raise TypeError("Input must be a string")
    
    # Use os.path.splitext to separate the filename and extension
    _, extension = os.path.splitext(file_path)
    
    # Remove the dot and return the extension (lowercase for consistency)
    return extension.lstrip('.').lower()