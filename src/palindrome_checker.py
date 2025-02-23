def is_palindrome(input_string: str) -> bool:
    """
    Check if the input string is a palindrome.
    
    Args:
        input_string (str): The string to check for palindrome property
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Notes:
        - The function is case-sensitive
        - Special characters and numbers are considered in the palindrome check
    """
    # If input is not a string, raise a TypeError
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove whitespace and convert to list for easy comparison
    comparison_string = list(input_string)
    
    # Compare the string forward and backward
    return comparison_string == comparison_string[::-1]