def is_numeric_string(input_string):
    """
    Check if a string contains only digits.
    
    Args:
        input_string (str): The string to validate.
    
    Returns:
        bool: True if the string contains only digits, False otherwise.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check if the string is empty
    if not input_string:
        return False
    
    # Use str.isdigit() to check if all characters are digits
    return input_string.isdigit()