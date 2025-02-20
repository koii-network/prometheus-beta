def is_palindrome(s: str) -> bool:
    """
    Determine if the input string is a palindrome.
    
    A palindrome is a string that reads the same backward as forward,
    ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Raises:
        TypeError: If input is not a string
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the string with its reverse
    return cleaned == cleaned[::-1]