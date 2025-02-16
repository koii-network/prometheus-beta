def is_palindrome_number(number):
    """
    Check if a given number is a palindrome.
    
    A palindrome number reads the same backwards as forwards.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is a palindrome, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Convert number to string for easy comparison
    num_str = str(abs(number))
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]