def convert_to_inverse_case(input_string: str) -> str:
    """
    Convert a string to inverse case.
    Each character's case is flipped: uppercase becomes lowercase and vice versa.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to inverse case
    
    Examples:
        >>> convert_to_inverse_case("Hello World")
        'hELLO wORLD'
        >>> convert_to_inverse_case("PyThOn")
        'pYtHoN'
        >>> convert_to_inverse_case("")
        ''
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return ''.join(char.lower() if char.isupper() else char.upper() for char in input_string)