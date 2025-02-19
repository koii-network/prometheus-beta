def find_primes_in_range(a: int, b: int) -> list:
    """
    Find all prime numbers between a and b (inclusive).
    
    Args:
        a (int): Lower bound of the range
        b (int): Upper bound of the range
    
    Returns:
        list: A list of prime numbers in the given range
    
    Raises:
        ValueError: If a or b are negative, or if a > b
    """
    # Validate input
    if a < 0 or b < 0:
        raise ValueError("Both a and b must be non-negative integers")
    
    if a > b:
        raise ValueError("Lower bound a must be less than or equal to upper bound b")
    
    # Helper function to check if a number is prime
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Find primes in the range
    return [num for num in range(max(2, a), b + 1) if is_prime(num)]