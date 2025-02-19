def triangle_number(num):
    """
    Determines if a number is a Triangle Number.
    
    A Triangle Number is a number that can be represented as the sum of its proper divisors.
    Proper divisors are positive integers that evenly divide the number (excluding the number itself).
    
    Args:
        num (int): The number to check for being a Triangle Number.
    
    Returns:
        bool: True if the number is a Triangle Number, False otherwise.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Find proper divisors
    proper_divisors = [divisor for divisor in range(1, num) if num % divisor == 0]
    
    # Calculate sum of proper divisors
    divisor_sum = sum(proper_divisors)
    
    # Check if sum of proper divisors equals the original number
    return divisor_sum == num