def convert_to_inverse_case(text: str) -> str:
    """
    Convert a string to inverse case (swap uppercase and lowercase).
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string with its case inverted.
    
    Examples:
        >>> convert_to_inverse_case("Hello World")
        'hELLO wORLD'
        >>> convert_to_inverse_case("Python 3.9")
        'pYTHON 3.9'
        >>> convert_to_inverse_case("")
        ''
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return ''.join(char.lower() if char.isupper() else char.upper() for char in text)