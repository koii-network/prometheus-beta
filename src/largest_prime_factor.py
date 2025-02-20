def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given positive integer.
    
    Args:
        n (int): A large positive integer greater than 1
    
    Returns:
        int: The largest prime factor of n
    
    Raises:
        ValueError: If n is less than or equal to 1
    """
    if n <= 1:
        raise ValueError("Input must be a positive integer greater than 1")
    
    # Initialize the largest prime factor
    largest_prime_factor = 1
    
    # First, handle the case of even numbers
    while n % 2 == 0:
        largest_prime_factor = 2
        n = n // 2
    
    # Now check for odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_prime_factor = factor
            n = n // factor
        factor += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        largest_prime_factor = n
    
    return largest_prime_factor