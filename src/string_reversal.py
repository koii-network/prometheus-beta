def recursive_reverse_string(s: str) -> str:
    """
    Recursively reverse a string.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Type checking
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: first character moved to end, recursively process the rest
    return recursive_reverse_string(s[1:]) + s[0]