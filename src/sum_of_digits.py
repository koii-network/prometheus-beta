def sum_of_digits(number):
    """
    Calculate the sum of digits for a positive integer.
    
    Args:
        number (int): A positive integer.
    
    Returns:
        int: Sum of all digits in the number.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Convert number to string to easily iterate through digits
    return sum(int(digit) for digit in str(number))