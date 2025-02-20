def is_palindrome(s: str) -> bool:
    """
    Determines if the input string is a palindrome.
    
    A palindrome is a string that reads the same backward as forward,
    ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned == cleaned[::-1]