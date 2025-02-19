def get_prime_factors(n):
    """
    Calculate the prime factors of a positive integer in ascending order.
    
    Args:
        n (int): A positive integer to factor.
    
    Returns:
        list: A sorted list of prime factors.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Input validation
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring while divisor squared is less than or equal to n
    while divisor * divisor <= n:
        # If n is divisible by divisor, add it to factors and divide n
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            # If not divisible, increment divisor
            divisor += 1
    
    # If n is greater than 1, it is a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors