def convert_to_uppercase(input_string):
    """
    Convert a given string to uppercase.

    Args:
        input_string (str): The string to be converted to uppercase.

    Returns:
        str: The input string converted to uppercase.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert and return the string to uppercase
    return input_string.upper()