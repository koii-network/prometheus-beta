def is_digit_string(input_string: str) -> bool:
    """
    Check if a string contains only digits.
    
    Args:
        input_string (str): The string to check.
    
    Returns:
        bool: True if the string contains only digits, False otherwise.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.isdigit()