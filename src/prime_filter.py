def filter_primes(numbers):
    """
    Filter a list of integers to return only prime numbers.
    
    A prime number is a number greater than 1 that has no divisors 
    other than 1 and itself.
    
    Args:
        numbers (list): A list of integers to filter
    
    Returns:
        list: A new list containing only prime numbers from the input list
    """
    def is_prime(n):
        # Numbers less than 2 are not prime
        if n < 2:
            return False
        
        # Check for divisibility from 2 to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    return [num for num in numbers if is_prime(num)]