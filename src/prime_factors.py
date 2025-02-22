def get_prime_factors(n):
    """
    Returns the prime factors of a positive integer in ascending order.
    
    Args:
        n (int): A positive integer to factorize
    
    Returns:
        list: A sorted list of prime factors
    
    Raises:
        ValueError: If input is not a positive integer
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special case for 1
    if n == 1:
        return []
    
    # Initialize list to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring until divisor > sqrt(n)
    while divisor * divisor <= n:
        # If divisor divides n evenly, add to factors
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            # If not divisible, increment divisor
            divisor += 1
    
    # If n is still > 1, it's a prime factor itself
    if n > 1:
        factors.append(n)
    
    return sorted(factors)