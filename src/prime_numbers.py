def get_primes_up_to_n(n: int) -> list[int]:
    """
    Return a list of all prime numbers from 1 to n (inclusive).
    
    Args:
        n (int): The upper limit to find prime numbers.
    
    Returns:
        list[int]: A list of prime numbers from 1 to n.
    """
    if n < 2:
        return []
    
    # Create a boolean array for Sieve of Eratosthenes 
    # Initialize all numbers as potentially prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes algorithm to mark non-primes
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark multiples of i as non-prime
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Collect and return all prime numbers
    return [num for num in range(2, n+1) if is_prime[num]]