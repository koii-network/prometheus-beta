def convert_to_inverse_case(text: str) -> str:
    """
    Convert a string to inverse case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string with case inverted (uppercase to lowercase and vice versa).
    
    Examples:
        >>> convert_to_inverse_case('Hello World')
        'hELLO wORLD'
        >>> convert_to_inverse_case('Python 3.9')
        'pYTHON 3.9'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return text.swapcase()