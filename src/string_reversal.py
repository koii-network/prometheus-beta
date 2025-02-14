def reverse_string(input_string):
    """
    Reverse the given string.
    
    Args:
        input_string (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Reverse the string
    return input_string[::-1]