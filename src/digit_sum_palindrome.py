def is_digit_sum_palindrome(n: int) -> bool:
    """
    Determines if the sum of the digits of a number is a palindrome.
    
    Args:
        n (int): The input integer
    
    Returns:
        bool: True if the sum of digits is a palindrome, False otherwise
    
    Raises:
        ValueError: If the input is a negative number
    """
    # Validate input
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(abs(n)))
    
    # Convert sum to string and check if it's a palindrome
    return str(digit_sum) == str(digit_sum)[::-1]