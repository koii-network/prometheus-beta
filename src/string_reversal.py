def recursive_reverse_string(s: str) -> str:
    """
    Recursively reverse a string containing only lowercase, uppercase letters, and spaces.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        ValueError: If input contains characters other than letters and spaces
    """
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Validate input contains only letters and spaces
    if not all(char.isalpha() or char.isspace() for char in s):
        raise ValueError("Input must contain only letters and spaces")
    
    # Recursive case: first character moved to the end, rest of string recursively reversed
    return recursive_reverse_string(s[1:]) + s[0]