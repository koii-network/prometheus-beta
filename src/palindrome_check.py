def is_palindrome_number(number):
    """
    Check if a given number is a palindrome.
    
    A palindrome number reads the same backward as forward.
    Negative numbers are not considered palindromes due to the minus sign.
    
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
    
    # Negative numbers are not palindromes
    if number < 0:
        return False
    
    # Convert number to string for easier comparison
    num_str = str(number)
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]