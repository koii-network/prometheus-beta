def sum_digits(number):
    """
    Calculate the sum of digits for a given number.
    
    Args:
        number (int): The input number to sum its digits.
    
    Returns:
        int: The sum of all digits in the number.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # First, validate input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Convert the number to its absolute value to handle negative numbers
    number = abs(number)
    
    # If number is 0, return 0
    if number == 0:
        return 0
    
    # Sum the digits
    total = 0
    while number > 0:
        total += number % 10  # Get the last digit
        number //= 10  # Remove the last digit
    
    return total