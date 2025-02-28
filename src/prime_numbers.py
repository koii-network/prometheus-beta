def get_primes_to_100():
    """
    Return a list of all prime numbers from 1 to 100.
    
    Returns:
        list: A list of prime numbers between 1 and 100 (inclusive).
    """
    # Handle edge cases
    if 100 < 2:
        return []
    
    # Initialize a list to track primality
    is_prime = [True] * (101)
    is_prime[0] = is_prime[1] = False
    
    # Sieve of Eratosthenes algorithm
    for i in range(2, int(100**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, 101, i):
                is_prime[j] = False
    
    # Collect prime numbers
    return [num for num in range(2, 101) if is_prime[num]]