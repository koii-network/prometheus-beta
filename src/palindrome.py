import re

def is_palindrome(input_string: str) -> bool:
    """
    Check if the given string is a palindrome, ignoring spaces, punctuation, and capitalization.
    
    Args:
        input_string (str): The string to check for palindrome properties.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string.lower())
    
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]