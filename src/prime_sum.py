def sum_of_primes(n):
    """
    Calculate the sum of all prime numbers up to and including the given integer.
    
    Args:
        n (int): The upper limit for finding prime numbers.
    
    Returns:
        int: The sum of all prime numbers less than or equal to n.
    
    Raises:
        ValueError: If the input is less than 2.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be 2 or greater")
    
    # Use Sieve of Eratosthenes to find primes
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use the Sieve algorithm to mark non-primes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Sum all prime numbers
    return sum(i for i in range(2, n+1) if is_prime[i])