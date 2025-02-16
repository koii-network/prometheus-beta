def sum_digits(number):
    """
    Calculate the sum of digits for a given number.
    
    Args:
        number (int): The input number to sum its digits.
    
    Returns:
        int: The sum of all digits in the number.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Convert number to string to easily iterate through digits
    return sum(int(digit) for digit in str(abs(number)))