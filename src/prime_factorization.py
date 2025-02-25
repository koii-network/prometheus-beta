def prime_factorize(n):
    """
    Perform prime factorization on a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        tuple: A tuple of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special cases
    if n == 1:
        return ()
    
    # Prime factorization algorithm
    factors = []
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    # If n is a prime number greater than 1
    if n > 1:
        factors.append(n)
    
    return tuple(factors)