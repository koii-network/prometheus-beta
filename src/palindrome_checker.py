import re

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces and special characters.
    
    Args:
        s (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove spaces and special characters, convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]