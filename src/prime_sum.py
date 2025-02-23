def sum_primes_under_n(n):
    """
    Calculate the sum of all prime numbers less than a given positive integer n.
    
    Args:
        n (int): A positive integer 
    
    Returns:
        int: The sum of all prime numbers less than n
    
    Raises:
        ValueError: If n is not a positive integer
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n <= 1:
        return 0
    
    # Use Sieve of Eratosthenes to find primes
    # Create a boolean array "is_prime[0..n]" and initialize 
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve algorithm to mark non-primes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    # Sum all prime numbers
    return sum(i for i in range(n) if is_prime[i])