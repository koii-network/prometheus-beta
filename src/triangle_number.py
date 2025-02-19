def triangle_number(num):
    """
    Determine if a number is a Triangle Number.
    
    A Triangle Number is a number that can be represented as the sum of its proper divisors.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is a Triangle Number, False otherwise.
    """
    # Input validation
    if not isinstance(num, int) or num <= 0:
        return False
    
    # Find proper divisors and sum them
    proper_divisors = [d for d in range(1, num) if num % d == 0]
    divisor_sum = sum(proper_divisors)
    
    # Check if the sum of proper divisors equals the input number
    return divisor_sum == num