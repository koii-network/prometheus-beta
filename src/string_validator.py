def is_numeric_string(s: str) -> bool:
    """
    Check if a string contains only digits.
    
    Args:
        s (str): The input string to validate.
    
    Returns:
        bool: True if the string contains only digits, False otherwise.
    
    Examples:
        >>> is_numeric_string('12345')
        True
        >>> is_numeric_string('123.45')
        False
        >>> is_numeric_string('')
        False
        >>> is_numeric_string('-123')
        False
    """
    if not s:  # Handle empty string
        return False
    
    return s.isdigit()