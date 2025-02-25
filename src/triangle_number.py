def triangle_number(num):
    """
    Determine if a number is a Triangle Number by summing its proper divisors.
    
    A Triangle Number is a number that can be represented as the sum of its 
    proper divisors (all positive divisors excluding the number itself).
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is a Triangle Number, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is not a positive integer.
    
    Examples:
        >>> triangle_number(6)  # 1 + 2 + 3 = 6
        True
        >>> triangle_number(12)  # 1 + 2 + 3 + 4 + 6 = 16 (not a triangle number)
        False
    """
    # Validate input
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    if num <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Find proper divisors and sum them
    proper_divisors = [i for i in range(1, num) if num % i == 0]
    divisor_sum = sum(proper_divisors)
    
    # Check if the sum of proper divisors equals the original number
    return divisor_sum == num