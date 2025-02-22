def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.
    
    A palindrome is a string that reads the same backward as forward,
    ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Raises:
        TypeError: If input is not a string
    """
    # Validate input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]