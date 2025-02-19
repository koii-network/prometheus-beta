def find_primes_in_range(a: int, b: int) -> list[int]:
    """
    Find all prime numbers in the given range (inclusive).
    
    Args:
        a (int): Lower bound of the range
        b (int): Upper bound of the range
    
    Returns:
        list[int]: List of prime numbers in the range
    
    Raises:
        ValueError: If a is greater than b or either input is negative
    """
    # Validate input
    if a < 0 or b < 0:
        raise ValueError("Input numbers must be non-negative")
    
    if a > b:
        raise ValueError("Lower bound must be less than or equal to upper bound")
    
    # Initialize result list
    primes = []
    
    # Check each number in the range
    for num in range(max(2, a), b + 1):
        # Assume number is prime until proven otherwise
        is_prime = True
        
        # Check for divisibility up to square root of the number
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        
        # If prime, add to result list
        if is_prime:
            primes.append(num)
    
    return primes