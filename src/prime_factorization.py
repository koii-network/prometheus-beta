def prime_factorize(n):
    """
    Perform prime factorization on a given number.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        tuple: A tuple of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is less than 2.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than or equal to 2")
    
    # List to store prime factors
    factors = []
    
    # Handle 2 as a special case first
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd prime factors
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            factors.append(factor)
            n = n // factor
        else:
            factor += 2
    
    # If n is still greater than 2, it means n itself is a prime factor
    if n > 2:
        factors.append(n)
    
    return tuple(factors)