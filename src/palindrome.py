import re

def is_palindrome(text: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces, punctuation, and capitalization.
    
    Args:
        text (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]