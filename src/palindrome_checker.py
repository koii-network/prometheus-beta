import re

def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome, ignoring case, punctuation, and spaces.
    
    Args:
        s (str): Input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]