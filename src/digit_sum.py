def sum_digits(number):
    """
    Calculate the sum of digits in a given number.

    Args:
        number (int): The input number whose digits will be summed.

    Returns:
        int: The sum of all digits in the input number.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.

    Examples:
        >>> sum_digits(123)
        6
        >>> sum_digits(0)
        0
        >>> sum_digits(9876)
        30
    """
    # Validate input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Validate input is non-negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle special case of 0
    if number == 0:
        return 0
    
    # Convert number to absolute value to handle potential edge cases
    number = abs(number)
    
    # Sum the digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    
    return digit_sum