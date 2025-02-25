def reverse_string(s: str) -> str:
    """
    Recursively reverse a given string.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: first character moved to end, rest of string reversed
    return reverse_string(s[1:]) + s[0]