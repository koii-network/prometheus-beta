import re

def is_palindrome(s: str) -> bool:
    """
    Determine whether a given string is a palindrome.
    
    A palindrome reads the same backward as forward, ignoring:
    - Spaces
    - Punctuation
    - Case sensitivity
    
    Args:
        s (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]