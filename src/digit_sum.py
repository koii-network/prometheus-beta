def sum_digits(number):
    """
    Calculate the sum of digits for a given integer.
    
    Args:
        number (int): The input number whose digits will be summed.
    
    Returns:
        int: The sum of all digits in the number.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check if input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Handle negative numbers by converting to absolute value
    number = abs(number)
    
    # Convert number to string to easily iterate through digits
    return sum(int(digit) for digit in str(number))