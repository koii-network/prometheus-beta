def generate_primes(n):
    """
    Generate all prime numbers from 1 to n using the Sieve of Eratosthenes algorithm.
    
    Args:
        n (int): The upper limit for prime number generation.
    
    Returns:
        list: A list of prime numbers from 1 to n.
    """
    # Handle edge cases
    if n < 2:
        return []
    
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
    
    # Collect and return prime numbers
    return [num for num in range(2, n+1) if is_prime[num]]