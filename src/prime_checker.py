def is_prime(number):
    """
    Determine whether an input integer between 2 and 1000 is a prime number.
    
    Args:
        number (int): An integer to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        ValueError: If the number is not between 2 and 1000.
    """
    # Validate input range
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    if number < 2 or number > 1000:
        raise ValueError("Number must be between 2 and 1000")
    
    # Special case: 2 is prime
    if number == 2:
        return True
    
    # Even numbers greater than 2 are not prime
    if number % 2 == 0:
        return False
    
    # Check odd numbers up to the square root of the number
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    
    return True