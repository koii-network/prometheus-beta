import re

def is_palindrome(s: str) -> bool:
    """
    Determine if a given string is a palindrome.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Check if the cleaned string reads the same forward and backward
    return cleaned_string == cleaned_string[::-1]