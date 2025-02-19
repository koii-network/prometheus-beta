def convert_to_inverse_case(input_string):
    """
    Convert a string to inverse case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string with its case inverted (uppercase becomes lowercase and vice versa).
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.swapcase()