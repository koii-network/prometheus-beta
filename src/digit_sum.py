def sum_of_digits(number: int) -> int:
    """
    Calculate the sum of digits for a given positive integer.

    Args:
        number (int): A positive integer to sum the digits of.

    Returns:
        int: The sum of all digits in the input number.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input is a positive integer
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    if number < 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special case of 0
    if number == 0:
        return 0
    
    # Convert number to positive to handle any potential signed input
    number = abs(number)
    
    # Sum the digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    
    return digit_sum