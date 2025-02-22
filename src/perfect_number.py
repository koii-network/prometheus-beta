def is_perfect_number(num):
    """
    Check if a given number is a perfect number.
    
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect number, False otherwise.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Find the sum of proper divisors
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    
    # Check if the sum of divisors equals the number
    return divisor_sum == num