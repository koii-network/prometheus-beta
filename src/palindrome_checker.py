import re

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring spaces, punctuation, and letter case.
    
    Args:
        s (str): Input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]