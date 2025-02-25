def find_primes_below_n(n):
    """
    Find all prime numbers below a given number n.
    
    Args:
        n (int): The upper limit (exclusive) for finding prime numbers.
    
    Returns:
        list: A list of prime numbers less than n.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n < 2:
        return []
    
    # Use the Sieve of Eratosthenes algorithm for efficient prime finding
    # Create a boolean array "is_prime[0..n]" and initialize all entries as true
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Use the sieve algorithm to mark non-prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    # Collect and return all prime numbers
    return [num for num in range(2, n) if is_prime[num]]