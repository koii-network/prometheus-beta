def is_digit_sum_palindrome(n: int) -> bool:
    """
    Determine if the sum of digits of the given integer is a palindrome number.
    
    Args:
        n (int): The input integer to check.
    
    Returns:
        bool: True if the sum of digits forms a palindrome, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.
    
    Examples:
        >>> is_digit_sum_palindrome(56)  # 5+6 = 11 (palindrome)
        True
        >>> is_digit_sum_palindrome(98)  # 9+8 = 17 (not a palindrome)
        False
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Calculate sum of digits
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Convert sum to string and check if it's a palindrome
    str_sum = str(digit_sum)
    return str_sum == str_sum[::-1]