def get_prime_factors(n):
    """
    Calculate the prime factors of a positive integer in ascending order.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A sorted list of prime factors.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return []
    
    # List to store prime factors
    factors = []
    
    # Check for divisibility by 2 first
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check odd factors up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n = n // factor
        factor += 2
    
    # If n is a prime factor greater than 2
    if n > 2:
        factors.append(n)
    
    return factors