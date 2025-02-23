def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome with complete case and character sensitivity.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("RaceCar")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        False
        >>> is_palindrome("")
        True
    """
    return s == s[::-1]