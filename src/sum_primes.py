def sum_of_primes(n):
    """
    Calculate the sum of all prime numbers up to and including the given integer.
    
    Args:
        n (int): The upper limit to calculate prime sum.
    
    Returns:
        int: Sum of all prime numbers up to and including n.
    
    Raises:
        ValueError: If input is less than 2.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be at least 2")
    
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Sum all prime numbers
    return sum(i for i in range(2, n+1) if is_prime[i])