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
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        return []
    
    # Use Sieve of Eratosthenes algorithm for efficient prime finding
    # Create a boolean array "is_prime[0..n]" and initialize 
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Use the Sieve algorithm to mark non-primes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    # Collect all prime numbers
    return [num for num in range(2, n) if is_prime[num]]