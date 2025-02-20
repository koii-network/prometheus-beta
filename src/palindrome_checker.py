def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces, punctuation, and case.
    
    Args:
        s (str): Input string to check for palindrome property
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("12321")
        True
        >>> is_palindrome("Hello, World!")
        False
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned_s == cleaned_s[::-1]