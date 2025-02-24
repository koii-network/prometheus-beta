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
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]