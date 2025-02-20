def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces, punctuation, and letter case.
    
    Args:
        s (str): Input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_s == cleaned_s[::-1]