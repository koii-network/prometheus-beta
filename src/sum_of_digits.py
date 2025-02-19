def sum_of_digits(number: int) -> int:
    """
    Calculate the sum of digits for a positive integer.
    
    Args:
        number (int): A positive integer to sum the digits of.
    
    Returns:
        int: The sum of all digits in the input number.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input is a positive integer
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Convert number to string and sum the digits
    return sum(int(digit) for digit in str(number))