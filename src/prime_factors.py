def get_prime_factors(n):
    """
    Return the prime factors of a positive integer in ascending order.
    
    Args:
        n (int): A positive integer greater than 1
    
    Returns:
        list: A sorted list of prime factors
    
    Raises:
        ValueError: If input is less than 2
        TypeError: If input is not an integer
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than 1")
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring until divisor squared exceeds n
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Add divisor to factors
            factors.append(divisor)
            # Divide n by divisor
            n //= divisor
        else:
            # If not divisible, move to next potential divisor
            divisor += 1
    
    # If n is greater than 1, it means n itself is prime
    if n > 1:
        factors.append(n)
    
    return factors