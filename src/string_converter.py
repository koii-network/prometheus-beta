def convert_to_lowercase_with_spaces(input_string):
    """
    Convert a string to lowercase, preserving spaces.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The lowercase version of the input string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.lower()