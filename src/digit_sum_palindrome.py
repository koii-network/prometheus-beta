def is_digit_sum_palindrome(n: int) -> bool:
    """
    Determines if the sum of digits of a given integer is a palindrome number.
    
    Args:
        n (int): The input integer to check.
    
    Returns:
        bool: True if the sum of digits is a palindrome, False otherwise.
    
    Raises:
        ValueError: If the input is a negative number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Convert the sum to a string for palindrome check
    digit_sum_str = str(digit_sum)
    
    # Check if the sum is a palindrome
    return digit_sum_str == digit_sum_str[::-1]