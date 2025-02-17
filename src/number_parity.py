def determine_parity(number):
    """
    Determine if a given number is even or odd.
    
    Args:
        number (int): The number to check for parity.
    
    Returns:
        str: 'even' if the number is even, 'odd' if the number is odd.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    return 'even' if number % 2 == 0 else 'odd'