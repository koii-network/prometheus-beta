def convert_to_inverse_case(input_string):
    """
    Convert a string to inverse case, where lowercase becomes uppercase 
    and uppercase becomes lowercase.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The string converted to inverse case.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a list comprehension with swapcase to convert each character
    return ''.join(char.swapcase() for char in input_string)