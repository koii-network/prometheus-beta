def get_primes_up_to(n):
    """
    Return a list of all prime numbers from 1 to n (inclusive).
    
    Args:
        n (int): The upper limit to find prime numbers.
    
    Returns:
        list: A list of prime numbers from 1 to n.
    """
    # Special case handling
    if n < 2:
        return []
    
    # Initialize a boolean array to track prime numbers
    # Using the Sieve of Eratosthenes algorithm
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    # Mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    # Collect prime numbers
    return [num for num in range(2, n+1) if primes[num]]