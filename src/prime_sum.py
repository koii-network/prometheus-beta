def sum_primes_under_n(n):
    """
    Calculate the sum of all prime numbers less than a given positive integer n.
    
    Args:
        n (int): The upper limit (exclusive) for finding prime numbers
    
    Returns:
        int: The sum of all prime numbers strictly less than n
    
    Raises:
        ValueError: If n is not a positive integer
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 1:
        return 0
    
    # Use Sieve of Eratosthenes to efficiently find primes
    # Initialize all numbers as potential primes
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Mark non-primes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    # Sum the primes
    return sum(num for num in range(2, n) if is_prime[num])