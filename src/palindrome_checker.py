def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.
    
    A palindrome is a string that reads the same backwards as forwards,
    ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the string with its reverse
    return cleaned_str == cleaned_str[::-1]