def sum_primes_under_n(n):
    """
    Calculate the sum of all prime numbers less than a given positive integer n.
    
    Args:
        n (int): A positive integer 
    
    Returns:
        int: Sum of all prime numbers less than n
    
    Raises:
        ValueError: If n is not a positive integer
    """
    # Check for invalid input
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be a positive integer greater than 1")
    
    # Create a boolean array "is_prime[0..n]" and initialize 
    # all entries as true. A value in is_prime[i] will 
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i*i, n, i):
                is_prime[j] = False
    
    # Sum all prime numbers less than n
    return sum(i for i in range(2, n) if is_prime[i])