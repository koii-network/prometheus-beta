def find_primes(start=1, end=100):
    """
    Find all prime numbers in the given range (inclusive).
    
    Args:
        start (int, optional): Starting number of the range. Defaults to 1.
        end (int, optional): Ending number of the range. Defaults to 100.
    
    Returns:
        list: A list of prime numbers in the specified range.
    """
    if start < 1:
        raise ValueError("Start of range must be at least 1")
    if end < start:
        raise ValueError("End of range must be greater than or equal to start")
    
    primes = []
    for num in range(max(2, start), end + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    return primes