import re

def to_snake_case(input_string):
    """
    Convert a given string to snake_case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to snake_case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Replace any non-alphanumeric characters with a space
    string = re.sub(r'[^a-zA-Z0-9]', ' ', input_string)
    
    # Replace multiple spaces with a single space
    string = re.sub(r'\s+', ' ', string)
    
    # Convert to lowercase
    string = string.lower()
    
    # Replace spaces with underscores
    string = string.replace(' ', '_')
    
    return string