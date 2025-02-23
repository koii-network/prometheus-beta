def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given positive integer.
    
    Args:
        n (int): A large positive integer 
    
    Returns:
        int: The largest prime factor of n
    
    Raises:
        ValueError: If input is less than 2
    """
    # Validate input
    if not isinstance(n, int) or n < 2:
        raise ValueError("Input must be a positive integer greater than or equal to 2")
    
    # Initialize largest prime factor
    largest_prime_factor = 1
    
    # First, handle even numbers by dividing out 2
    while n % 2 == 0:
        largest_prime_factor = 2
        n = n // 2
    
    # Now check for odd factors up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_prime_factor = factor
            n = n // factor
        factor += 2
    
    # If n is a prime number larger than the current largest factor
    if n > largest_prime_factor:
        largest_prime_factor = n
    
    return largest_prime_factor