import re

def contains_palindrome_word(input_string):
    """
    Determine if the input string contains a palindrome word.
    
    Args:
        input_string (str): A string containing words, numbers, and special characters.
    
    Returns:
        bool: True if the string contains a palindrome word, False otherwise.
    """
    # Remove special characters and split into words
    words = re.findall(r'\b[a-zA-Z]+\b', input_string)
    
    # Check each word if it's a palindrome
    for word in words:
        # Convert to lowercase for case-insensitive palindrome check
        clean_word = word.lower()
        if clean_word == clean_word[::-1]:
            return True
    
    return False