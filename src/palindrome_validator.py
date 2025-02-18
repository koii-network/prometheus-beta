import re

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a valid palindrome, ignoring spaces and punctuation.
    
    Args:
        s (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned == cleaned[::-1]