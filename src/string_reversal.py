def recursive_reverse_string(s: str) -> str:
    """
    Recursively reverse a string containing lowercase, uppercase letters, and spaces.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed input string
    
    Raises:
        TypeError: If input is not a string
    """
    # Check for invalid input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: move first character to the end of the reversed rest of the string
    return recursive_reverse_string(s[1:]) + s[0]