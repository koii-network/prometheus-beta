def generate_primes(limit=100):
    """
    Generate all prime numbers from 2 to the given limit (inclusive).
    
    Args:
        limit (int, optional): Upper limit for prime number generation. Defaults to 100.
    
    Returns:
        list: A list of prime numbers from 2 to the limit.
    """
    # Handle edge cases
    if limit < 2:
        return []
    
    # Use Sieve of Eratosthenes algorithm for efficient prime generation
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as not prime
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    
    # Return list of prime numbers
    return [num for num in range(2, limit + 1) if sieve[num]]