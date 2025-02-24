def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given positive integer.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        int: The largest prime factor of the input number.

    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than 1")
    
    # Initialize the largest prime factor
    largest_prime_factor = 1
    
    # First, handle even numbers by dividing out 2
    while n % 2 == 0:
        largest_prime_factor = 2
        n = n // 2
    
    # Now check for odd factors
    # We only need to check up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        # While factor divides n completely
        while n % factor == 0:
            largest_prime_factor = factor
            n = n // factor
        
        # Move to next potential prime factor
        factor += 2
    
    # If n is a prime number larger than the last factor
    if n > 2:
        largest_prime_factor = n
    
    return largest_prime_factor