def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given positive integer.
    
    Args:
        n (int): A large positive integer to factorize.
    
    Returns:
        int: The largest prime factor of the input number.
    
    Raises:
        ValueError: If the input is less than or equal to 1.
        TypeError: If the input is not an integer.
    
    Examples:
        >>> find_largest_prime_factor(13195)
        29
        >>> find_largest_prime_factor(600851475143)
        6857
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 1:
        raise ValueError("Input must be a positive integer greater than 1")
    
    # Initialize the largest prime factor
    largest_prime_factor = 1
    
    # Handle even numbers first
    while n % 2 == 0:
        largest_prime_factor = 2
        n //= 2
    
    # Check for odd factors
    factor = 3
    while factor * factor <= n:
        # If factor divides n, it's a factor
        while n % factor == 0:
            largest_prime_factor = factor
            n //= factor
        
        # Move to next potential factor
        factor += 2
    
    # If n is a prime number larger than the previous largest factor
    if n > largest_prime_factor:
        largest_prime_factor = n
    
    return largest_prime_factor