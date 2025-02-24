def find_primes(limit=100):
    """
    Find all prime numbers from 2 to the given limit (inclusive).
    
    Args:
        limit (int, optional): Upper limit for finding prime numbers. Defaults to 100.
    
    Returns:
        list: A list of prime numbers from 2 to the limit.
    """
    # Handle edge cases
    if limit < 2:
        return []
    
    # Use Sieve of Eratosthenes algorithm for efficient prime finding
    # Create a boolean array "is_prime[0..limit]" and initialize all entries as true
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    # Collect and return prime numbers
    return [num for num in range(2, limit + 1) if is_prime[num]]