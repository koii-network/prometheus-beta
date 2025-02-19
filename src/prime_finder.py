def find_primes_below_n(n):
    """
    Find all prime numbers below a given number n.
    
    Args:
        n (int): The upper limit (exclusive) for finding prime numbers.
    
    Returns:
        list: A list of prime numbers less than n.
    
    Raises:
        ValueError: If n is less than 2.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        return []
    
    # Initialize the sieve of Eratosthenes
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    
    # Mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n, i):
                sieve[j] = False
    
    # Collect prime numbers
    return [num for num in range(n) if sieve[num]]