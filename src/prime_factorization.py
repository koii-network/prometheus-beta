def prime_factorization(n: int) -> tuple[int, ...]:
    """
    Perform prime factorization on a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        tuple[int, ...]: A tuple of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    
    Examples:
        >>> prime_factorization(12)
        (2, 2, 3)
        >>> prime_factorization(17)
        (17,)
        >>> prime_factorization(100)
        (2, 2, 5, 5)
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than or equal to 2")
    
    # Prime factorization algorithm
    factors = []
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    
    # If n is a prime number greater than 1, add it to factors
    if n > 1:
        factors.append(n)
    
    return tuple(factors)