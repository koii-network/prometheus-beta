import re

def contains_palindrome_word(input_string):
    """
    Determine if the input string contains a palindrome word.
    
    Args:
        input_string (str): A string containing words, numbers, and special characters
    
    Returns:
        bool: True if the string contains a palindrome word, False otherwise
    
    Examples:
        >>> contains_palindrome_word("hello level world")
        True
        >>> contains_palindrome_word("python code")
        False
        >>> contains_palindrome_word("121 is a palindrome number")
        True
    """
    # Remove special characters and split into words
    words = re.findall(r'\b\w+\b', input_string.lower())
    
    # Check if any word is a palindrome
    for word in words:
        if word == word[::-1]:
            return True
    
    return False