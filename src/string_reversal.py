def recursive_string_reverse(s: str) -> str:
    """
    Recursively reverse a string containing lowercase, uppercase letters, and spaces.
    
    Args:
        s (str): Input string to be reversed
    
    Returns:
        str: Reversed string
    
    Raises:
        ValueError: If input contains characters other than letters and spaces
    """
    # Base case: if string is empty or has only one character, return it
    if len(s) <= 1:
        return s
    
    # Validate input to ensure only letters and spaces
    if not all(char.isalpha() or char.isspace() for char in s):
        raise ValueError("Input must contain only letters and spaces")
    
    # Recursive case: take the last character and put it at the start of the reversed substring
    return s[-1] + recursive_string_reverse(s[:-1])