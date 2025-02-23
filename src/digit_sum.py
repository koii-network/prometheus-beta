def sum_digits(number):
    """
    Calculate the sum of digits for a given integer.

    Args:
        number (int): The input number to sum digits of.

    Returns:
        int: The sum of all digits in the input number.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.
    """
    # Check input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check for negative numbers
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle zero as a special case
    if number == 0:
        return 0
    
    # Sum the digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10  # Get the rightmost digit
        number //= 10  # Remove the rightmost digit
    
    return digit_sum