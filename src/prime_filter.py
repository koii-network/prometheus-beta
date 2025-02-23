def is_prime(num):
    """
    Check if a given number is prime.
    
    Args:
        num (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check for invalid input
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    # Numbers less than 2 are not prime
    if num < 2:
        return False
    
    # Check for divisibility from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def filter_primes(numbers):
    """
    Filter a list of integers to return only prime numbers.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A new list containing only the prime numbers from the input.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Filter and return prime numbers
    return [num for num in numbers if is_prime(num)]