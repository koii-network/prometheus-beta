def is_prime(number):
    """
    Determine if a given number is prime.

    Args:
        number (int): A positive integer to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input type
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    # Validate input value
    if number != int(number) or number is None:
        raise ValueError("Input must be an integer")
    
    # Handle edge cases for non-positive numbers
    if number < 2:
        return False
    
    # Optimization: Check divisibility up to square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True