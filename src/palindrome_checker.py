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
        TypeError: If the input is not a string.
    """
    # Validate input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_s == cleaned_s[::-1]