def convert_to_lowercase(input_string):
    """
    Convert a given string to lowercase.
    
    Args:
        input_string (str): The string to be converted to lowercase.
    
    Returns:
        str: The lowercase version of the input string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.lower()