def sum_of_digits(num):
    """
    Calculate the sum of digits for a positive integer.
    
    Args:
        num (int): A positive integer.
    
    Returns:
        int: The sum of all digits in the input number.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Convert number to string to easily iterate through digits
    return sum(int(digit) for digit in str(num))