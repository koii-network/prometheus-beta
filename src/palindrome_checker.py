def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.
    
    A palindrome reads the same forwards and backwards, ignoring case, spaces, and punctuation.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]