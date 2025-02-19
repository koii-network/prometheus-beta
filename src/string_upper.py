def convert_to_upper_with_spaces(input_string):
    """
    Convert a string to upper case, preserving spaces.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to upper case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.upper()