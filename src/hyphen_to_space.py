def convert_hyphens_to_spaces(input_string: str) -> str:
    """
    Convert a hyphen-separated string to a space-separated string.
    
    Args:
        input_string (str): A string with hyphens
    
    Returns:
        str: A string with hyphens replaced by spaces
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.replace('-', ' ')