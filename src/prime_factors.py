def prime_factorization(n):
    """
    Returns a list of prime factors for a given positive integer.
    
    Args:
        n (int): A positive integer to factorize
    
    Returns:
        list: A list of prime factors in ascending order
    
    Raises:
        ValueError: If input is not a positive integer
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # List to store prime factors
    factors = []
    
    # Handle factor 2 separately for efficiency
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
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors