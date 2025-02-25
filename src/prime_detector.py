def is_prime(number: int) -> bool:
    """
    Determine whether an input integer is a prime number.

    Args:
        number (int): An integer to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        ValueError: If the input is not an integer between 2 and 1000.
    """
    # Validate input range
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    if number < 2 or number > 1000:
        raise ValueError("Input must be between 2 and 1000")
    
    # Optimization: Check for divisibility up to square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True