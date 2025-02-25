def sum_primes_up_to(n):
    """
    Calculate the sum of all prime numbers up to and including the given integer.
    
    Args:
        n (int): The upper limit (inclusive) for finding prime numbers.
    
    Returns:
        int: The sum of all prime numbers less than or equal to n.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n < 2:
        return 0
    
    # Use Sieve of Eratosthenes to find primes
    # Create a boolean array to mark primes
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Mark non-primes using Sieve of Eratosthenes algorithm
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Sum all prime numbers
    return sum(num for num in range(2, n+1) if is_prime[num])