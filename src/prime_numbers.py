def find_primes(start=1, end=100):
    """
    Find all prime numbers in the given range (inclusive).
    
    Args:
        start (int, optional): The starting number of the range. Defaults to 1.
        end (int, optional): The ending number of the range. Defaults to 100.
    
    Returns:
        list: A sorted list of prime numbers within the specified range.
    
    Raises:
        ValueError: If start is less than 1 or end is less than start.
    """
    # Validate input
    if start < 1:
        raise ValueError("Start must be a positive integer")
    if end < start:
        raise ValueError("End must be greater than or equal to start")
    
    # Use the Sieve of Eratosthenes algorithm for efficient prime finding
    # Create a boolean array "is_prime[0..end]" and initialize 
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes algorithm
    for i in range(2, int(end**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i*i, end + 1, i):
                is_prime[j] = False
    
    # Collect primes within the specified range
    return [num for num in range(max(2, start), end + 1) if is_prime[num]]