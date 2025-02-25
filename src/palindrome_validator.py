def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a valid palindrome, ignoring spaces, punctuation, and case.
    
    Args:
        s (str): The input string to check.
    
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
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]