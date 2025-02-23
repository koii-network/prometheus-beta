def is_prime(number: int) -> bool:
    """
    Determine if a given integer is a prime number.

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
    
    # Handle small prime cases quickly
    if number in (2, 3, 5, 7):
        return True
    
    # Quick even number check (except 2)
    if number % 2 == 0:
        return False
    
    # Check for divisibility up to square root of the number
    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    
    return True