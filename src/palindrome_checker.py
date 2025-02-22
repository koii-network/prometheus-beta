import re

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces and special characters.
    
    Args:
        s (str): Input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned_str == cleaned_str[::-1]