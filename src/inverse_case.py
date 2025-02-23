def convert_to_inverse_case(input_string):
    """
    Convert a string to inverse case (uppercase becomes lowercase and vice versa).

    Args:
        input_string (str): The input string to be converted to inverse case.

    Returns:
        str: The input string with its case inverted.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a list comprehension to swap the case of each character
    return ''.join(char.lower() if char.isupper() else char.upper() for char in input_string)