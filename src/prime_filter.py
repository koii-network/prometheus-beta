def is_prime(num):
    """
    Check if a given number is prime.
    
    A prime number is a positive integer greater than 1 that has no positive divisors 
    other than 1 and itself.
    
    Args:
        num (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than or equal to 0.
    """
    # Check input type
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    
    # Check for numbers less than or equal to 1
    if num <= 1:
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
        list: A new list containing only the prime numbers from the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Filter and return prime numbers
    return [num for num in numbers if is_prime(num)]