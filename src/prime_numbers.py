def generate_primes(max_num=100):
    """
    Generate a list of prime numbers from 1 to max_num (inclusive).
    
    Args:
        max_num (int, optional): The upper limit for prime number generation. 
                                 Defaults to 100.
    
    Returns:
        list: A list of prime numbers from 1 to max_num.
    """
    if max_num < 2:
        return []
    
    # Use the Sieve of Eratosthenes algorithm
    # Initialize the sieve
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    
    # Mark non-prime numbers
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, max_num + 1, i):
                sieve[j] = False
    
    # Collect prime numbers
    return [num for num in range(2, max_num + 1) if sieve[num]]