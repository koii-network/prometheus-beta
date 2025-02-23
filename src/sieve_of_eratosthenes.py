def sieve_of_eratosthenes(n):
    """
    Implement the Sieve of Eratosthenes algorithm to find all prime numbers up to n.
    
    Args:
        n (int): The upper limit to find prime numbers up to.
    
    Returns:
        list: A list of prime numbers less than or equal to n.
    
    Raises:
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Return empty list for inputs less than 2
    if n < 2:
        return []
    
    # Create a boolean array "is_prime[0..n]" and initialize 
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use the Sieve of Eratosthenes algorithm
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Collect and return prime numbers
    return [num for num in range(2, n+1) if is_prime[num]]