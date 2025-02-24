def generate_primes(max_num=100):
    """
    Generate all prime numbers from 2 up to the given maximum number.
    
    Args:
        max_num (int, optional): The upper limit for prime number generation. 
                                 Defaults to 100.
    
    Returns:
        list: A sorted list of prime numbers from 2 up to max_num.
    
    Raises:
        ValueError: If max_num is less than 2.
    """
    # Validate input
    if not isinstance(max_num, int):
        raise TypeError("Input must be an integer")
    
    if max_num < 2:
        raise ValueError("Maximum number must be at least 2")
    
    # Use Sieve of Eratosthenes algorithm for efficient prime generation
    # Create a boolean array "is_prime[0..max_num]" and initialize 
    # all entries it as true. A value in is_prime[i] will 
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes to mark non-primes
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i*i, max_num + 1, i):
                is_prime[j] = False
    
    # Collect all prime numbers
    return [num for num in range(2, max_num + 1) if is_prime[num]]