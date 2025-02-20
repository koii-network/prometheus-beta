def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome with complete case and character sensitivity.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Examples:
        - is_palindrome("racecar") returns True
        - is_palindrome("Racecar") returns False (case-sensitive)
        - is_palindrome("a") returns True
        - is_palindrome("") returns True
    """
    # Empty string or single character is always a palindrome
    if len(s) <= 1:
        return True
    
    # Compare characters from both ends moving inwards
    left, right = 0, len(s) - 1
    while left < right:
        # If characters don't match, it's not a palindrome
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True