def reverse_string(input_str):
    """
    Reverses a given string.
    
    Args:
        input_str (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    return input_str[::-1]