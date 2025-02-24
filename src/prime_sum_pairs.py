def is_prime(num):
    """
    Check if a given number is prime.
    
    Args:
        num (int): Number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_sum_pairs(n):
    """
    Generate unique prime numbers that can be obtained by summing pairs 
    of numbers from the range [1, n].
    
    Args:
        n (int): Upper bound of the range to generate pairs from.
    
    Returns:
        list: Sorted list of unique prime numbers obtained from summing pairs.
    
    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Input must be at least 2")
    
    # Use a set to ensure uniqueness of prime sums
    prime_sums = set()
    
    # Generate all possible pairs and their sums
    for i in range(1, n):
        for j in range(i, n + 1):
            pair_sum = i + j
            if is_prime(pair_sum) and pair_sum != n:
                prime_sums.add(pair_sum)
    
    # Return sorted list of unique prime sums
    return sorted(list(prime_sums))