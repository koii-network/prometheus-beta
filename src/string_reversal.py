def reverse_string(input_string: str) -> str:
    """
    Reverses the input string by returning its characters in reverse order.
    
    Args:
        input_string (str): The string to be reversed.
    
    Returns:
        str: The input string with characters in reverse order.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string[::-1]