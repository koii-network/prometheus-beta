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
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Convert negative numbers to positive for palindrome check
    number = abs(number)
    
    # Convert number to string for easy comparison
    str_number = str(number)
    
    # Compare the string with its reverse
    return str_number == str_number[::-1]