def recursive_reverse_string(s: str) -> str:
    """
    Recursively reverse a given string.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    # Base case: if string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    
    # Recursive case: first character moved to the end, rest of string reversed
    return recursive_reverse_string(s[1:]) + s[0]