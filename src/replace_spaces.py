def replace_spaces_with_underscores(input_string):
    """
    Replace all spaces in a given string with underscores.
    
    Args:
        input_string (str): The input string to modify.
    
    Returns:
        str: A new string with spaces replaced by underscores.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.replace(' ', '_')