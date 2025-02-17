def sum_digits(number):
    """
    Calculate the sum of digits in a given number.
    
    Args:
        number (int): The number whose digits need to be summed.
    
    Returns:
        int: The sum of all digits in the number.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if number == 0:
        return 0
    
    # Convert the number to its absolute value to handle negative inputs
    number = abs(number)
    
    # Sum the digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    
    return digit_sum