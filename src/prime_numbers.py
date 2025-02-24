def find_primes_up_to_n(n: int) -> list[int]:
    """
    Find all prime numbers from 1 to n using the Sieve of Eratosthenes algorithm.
    
    Args:
        n (int): The upper limit for finding prime numbers (inclusive).
    
    Returns:
        list[int]: A sorted list of prime numbers from 1 to n.
    
    Raises:
        ValueError: If n is negative or not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n < 2:
        return []
    
    # Initialize the sieve
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    # Mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    
    # Collect prime numbers
    return [num for num in range(2, n + 1) if sieve[num]]