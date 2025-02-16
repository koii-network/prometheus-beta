def is_perfect_number(n):
    """
    Check if a given number is a perfect number.
    
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors 
    (excluding the number itself).
    
    Args:
        n (int): The number to check
    
    Returns:
        bool: True if the number is a perfect number, False otherwise
    
    Raises:
        ValueError: If the input is not a positive integer
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    # Perfect numbers are positive
    if n <= 0:
        return False
    
    # Find the sum of proper divisors
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    
    # Check if the sum of divisors equals the number
    return divisor_sum == n