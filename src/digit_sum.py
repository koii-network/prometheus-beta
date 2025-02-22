def sum_digits(number):
    """
    Calculate the sum of digits for a given number.
    
    Args:
        number (int): The input number to sum digits for.
    
    Returns:
        int: The sum of all digits in the number.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input number is negative.
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Handle special case of 0
    if number == 0:
        return 0
    
    # Sum the digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    
    return digit_sum