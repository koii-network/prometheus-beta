def is_digit_sum_palindrome(n: int) -> bool:
    """
    Determine if the sum of digits of a given integer is a palindrome number.
    
    Args:
        n (int): The input integer to check.
    
    Returns:
        bool: True if the sum of digits is a palindrome, False otherwise.
    
    Raises:
        ValueError: If the input is a negative integer.
    """
    # Check for negative input
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Convert sum to string to check if it's a palindrome
    sum_str = str(digit_sum)
    
    # Check if the sum is a palindrome
    return sum_str == sum_str[::-1]