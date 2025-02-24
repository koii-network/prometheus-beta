def is_perfect_number(n):
    """
    Check if a given number is a perfect number.

    A perfect number is a positive integer that is equal to the sum of its proper divisors 
    (excluding the number itself). For example, 6 is a perfect number because 1 + 2 + 3 = 6.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is a perfect number, False otherwise.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    # Perfect numbers are positive integers greater than 0
    if n <= 0:
        return False
    
    # Find sum of proper divisors
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    
    # Check if sum of divisors equals the number
    return divisor_sum == n