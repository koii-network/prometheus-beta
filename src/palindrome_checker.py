def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.
    
    A palindrome is a string that reads the same backward as forward,
    ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]