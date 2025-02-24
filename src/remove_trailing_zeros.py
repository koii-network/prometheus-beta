def remove_trailing_zeros(number: int) -> int:
    """
    Remove all trailing zeros from the end of a non-negative integer.

    Args:
        number (int): A non-negative integer to remove trailing zeros from.

    Returns:
        int: The input number with all trailing zeros removed.

    Raises:
        ValueError: If the input is a negative number.

    Examples:
        >>> remove_trailing_zeros(10200)
        102
        >>> remove_trailing_zeros(123000)
        123
        >>> remove_trailing_zeros(0)
        0
    """
    # Validate input is non-negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if number == 0:
        return 0
    
    # Remove trailing zeros by integer division
    while number % 10 == 0:
        number //= 10
    
    return number