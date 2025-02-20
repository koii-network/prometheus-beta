def get_prime_factors(n):
    """
    Compute the prime factors of a positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A list of prime factors in ascending order.
    
    Raises:
        ValueError: If input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # List to store prime factors
    factors = []
    
    # Handle 2 as a special case first
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd prime factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n = n // factor
        factor += 2
    
    # If n is still greater than 1, it means n itself is a prime factor
    if n > 1:
        factors.append(n)
    
    return factors