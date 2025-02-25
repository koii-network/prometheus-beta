def convert_to_lowercase_with_spaces(input_string):
    """
    Convert a string to lowercase, preserving spaces.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The input string converted to lowercase.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase
    return input_string.lower()