import re

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a valid palindrome, ignoring spaces, punctuation, and case.
    
    Args:
        s (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]