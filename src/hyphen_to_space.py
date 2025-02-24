def replace_hyphens(input_string: str) -> str:
    """
    Replace hyphens in a given string with spaces.

    Args:
        input_string (str): A string potentially containing hyphens.

    Returns:
        str: A new string with hyphens replaced by spaces.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Replace hyphens with spaces
    return input_string.replace('-', ' ')