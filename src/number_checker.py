def is_even_or_odd(number):
    """
    Determine if a given number is even or odd.

    Args:
        number (int): The number to check.

    Returns:
        str: 'even' if the number is even, 'odd' if the number is odd.

    Raises:
        TypeError: If the input is not an integer.
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Return 'even' if number is divisible by 2 with no remainder, else 'odd'
    return 'even' if number % 2 == 0 else 'odd'