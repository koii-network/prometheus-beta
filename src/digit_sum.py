def sum_digits(number):
    """
    Calculate the sum of digits for a given number.
    
    Args:
        number (int): The input number to sum digits for.
    
    Returns:
        int: The sum of all digits in the number.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Validate input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Handle negative numbers by converting to positive
    number = abs(number)
    
    # Sum the digits
    return sum(int(digit) for digit in str(number))