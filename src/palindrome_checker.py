def is_palindrome_number(number):
    """
    Check if a given number is a palindrome.
    
    A palindrome number reads the same backward as forward.
    
    Args:
        number (int): The number to check for palindrome property.
    
    Returns:
        bool: True if the number is a palindrome, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    
    Examples:
        >>> is_palindrome_number(121)
        True
        >>> is_palindrome_number(-121)
        False
        >>> is_palindrome_number(10)
        False
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Negative numbers are not palindromes
    if number < 0:
        return False
    
    # Convert number to string for easy comparison
    num_str = str(number)
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]