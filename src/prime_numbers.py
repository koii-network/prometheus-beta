def get_primes(n):
    """
    Return a list of all prime numbers from 1 to n.
    
    Args:
        n (int): The upper limit to find prime numbers.
    
    Returns:
        list: A list of prime numbers from 1 to n.
    
    Raises:
        ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Use the Sieve of Eratosthenes algorithm
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    # Collect all prime numbers
    return [num for num in range(n + 1) if sieve[num]]