def reverse_string(s: str) -> str:
    """
    Reverse a given string.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    return s[::-1]