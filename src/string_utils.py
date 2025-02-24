def replace_spaces_with_underscores(input_string: str) -> str:
    """
    Replace all spaces in a given string with underscores.

    Args:
        input_string (str): The original string with spaces.

    Returns:
        str: A new string with spaces replaced by underscores.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Replace spaces with underscores
    return input_string.replace(' ', '_')