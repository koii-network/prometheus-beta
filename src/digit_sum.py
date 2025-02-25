def sum_of_digits(number: int) -> int:
    """
    Calculate the sum of digits for a given positive integer.

    Args:
        number (int): A positive integer to calculate digit sum for.

    Returns:
        int: The sum of all digits in the input number.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    if number < 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle zero as a special case
    if number == 0:
        return 0
    
    # Calculate sum of digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10  # Get the rightmost digit
        number //= 10  # Remove the rightmost digit
    
    return digit_sum