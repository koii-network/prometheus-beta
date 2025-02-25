def find_primes_in_range(a: int, b: int) -> list:
    """
    Find all prime numbers within the given range (inclusive).

    Args:
        a (int): Lower bound of the range
        b (int): Upper bound of the range

    Returns:
        list: A sorted list of prime numbers within the range

    Raises:
        ValueError: If inputs are not integers or if a > b
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    if a > b:
        raise ValueError("Lower bound must be less than or equal to upper bound")
    
    # Handle edge cases with small ranges
    if b < 2:
        return []
    
    # Initialize the sieve of Eratosthenes
    # Use b+1 to include the upper bound in potential primes
    sieve = [True] * (b + 1)
    sieve[0] = sieve[1] = False
    
    # Mark non-primes using Sieve of Eratosthenes algorithm
    for i in range(2, int(b**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, b+1, i):
                sieve[j] = False
    
    # Collect primes within the range
    primes = [num for num in range(max(2, a), b+1) if sieve[num]]
    
    return primes