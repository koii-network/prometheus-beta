def get_prime_factors(n):
    """
    Calculate the prime factors of a positive integer in ascending order.

    Args:
        n (int): A positive integer to factorize.

    Returns:
        list: A sorted list of prime factors of the input number.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special case for 1
    if n == 1:
        return []
    
    # Initialize list to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Find prime factors
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Add the divisor to factors
            factors.append(divisor)
            # Divide n by the divisor
            n //= divisor
        else:
            # If not divisible, move to next potential divisor
            divisor += 1
    
    # If n is greater than 1, it's a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors