import re

def contains_palindrome(input_string):
    """
    Determine if the input string contains a palindrome word.
    
    Args:
        input_string (str): A string containing a mix of words, numbers, and special characters.
    
    Returns:
        bool: True if the string contains a palindrome word, False otherwise.
    """
    # Remove special characters and split into words
    words = re.findall(r'\b\w+\b', input_string.lower())
    
    # Check each word for palindrome
    for word in words:
        # Ignore words shorter than 2 characters
        if len(word) > 1 and word == word[::-1]:
            return True
    
    return False