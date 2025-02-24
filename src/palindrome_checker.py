import re

def is_palindrome(s: str) -> bool:
    """
    Determine if a given string is a palindrome, ignoring spaces, punctuation, and case.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned_str == cleaned_str[::-1]