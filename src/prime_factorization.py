def prime_factorization(n):
    """
    Perform prime factorization on a given number.
    
    Args:
        n (int): The number to factorize. Must be a positive integer greater than 1.
    
    Returns:
        tuple: A tuple of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than 1")
    
    # Prime factorization algorithm
    factors = []
    
    # Check for 2 as a factor first
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd factors starting from 3
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            factors.append(factor)
            n = n // factor
        else:
            factor += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return tuple(factors)