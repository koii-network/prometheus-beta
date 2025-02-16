def find_primes_to_100():
    """
    Return a list of all prime numbers between 1 and 100 (inclusive).
    
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    
    Returns:
        list: A list of prime numbers from 1 to 100.
    """
    # Use the Sieve of Eratosthenes algorithm for efficient prime finding
    # Initialize a boolean array "is_prime[0..100]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * 101
    
    # 0 and 1 are not prime numbers
    is_prime[0] = is_prime[1] = False
    
    # Use the Sieve of Eratosthenes
    for i in range(2, int(100**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i*i, 101, i):
                is_prime[j] = False
    
    # Collect all prime numbers
    return [num for num in range(2, 101) if is_prime[num]]