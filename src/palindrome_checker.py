import re

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces, punctuation, and letter case.
    
    Args:
        s (str): Input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    clean_str = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Check if the cleaned string is equal to its reverse
    return clean_str == clean_str[::-1]