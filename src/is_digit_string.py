def is_digit_string(s: str) -> bool:
    """
    Check if a string contains only digits.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string contains only digits, False otherwise.
    """
    # Handle empty string case
    if not s:
        return False
    
    # Check if all characters are digits
    return s.isdigit()