def is_prime(n):
    """
    Check if a number is prime, handling both positive and negative numbers.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # 0, 1, and negative numbers are not prime
    if n <= 1:
        return False
    
    # Check for divisibility up to the square root of n
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def filter_primes(numbers):
    """
    Filter a list of numbers to return only prime numbers.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A list containing only the prime numbers from the input list.
    """
    return [num for num in numbers if is_prime(num)]