def is_prime(num):
    """
    Check if a given number is prime.
    
    Args:
        num (int): The number to check for primality.
    
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
    Generate a list of unique prime numbers that can be obtained by summing 
    pairs of numbers from the range [1, n].
    
    Args:
        n (int): The upper limit of the range to consider.
    
    Returns:
        list: A sorted list of unique prime numbers generated from sum pairs.
        
    Raises:
        ValueError: If n is less than 2.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be at least 2")
    
    # Set to store unique prime sums
    prime_sums = set()
    
    # Generate sum pairs and check which sums are prime
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if pair_sum <= 2 * n and is_prime(pair_sum):
                # Only add prime sums greater than or equal to 5
                if pair_sum >= 5:
                    prime_sums.add(pair_sum)
    
    # Return sorted list of unique prime sums
    return sorted(list(prime_sums))