def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome, ignoring spaces and special characters.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned_str == cleaned_str[::-1]