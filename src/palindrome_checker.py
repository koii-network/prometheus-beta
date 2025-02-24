def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.
    
    Args:
        s (str): Input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Description:
    - Ignores case
    - Ignores spaces
    - Works with letters and numbers
    """
    # Remove spaces and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the string with its reverse
    return cleaned_str == cleaned_str[::-1]