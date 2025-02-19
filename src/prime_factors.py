def get_prime_factors(n):
    """
    Returns the prime factors of a positive integer in ascending order.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A sorted list of prime factors.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    factors = []
    # Start with the smallest prime number
    divisor = 2
    
    # Continue until the divisor is greater than the square root of n
    while divisor * divisor <= n:
        if n % divisor == 0:
            # If divisible, add the factor and divide n
            factors.append(divisor)
            n //= divisor
        else:
            # If not divisible, increment the divisor
            divisor += 1
    
    # If n is still greater than 1, it's a prime factor itself
    if n > 1:
        factors.append(n)
    
    return sorted(factors)