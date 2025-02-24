def int_to_binary(number):
    """
    Convert an integer to its binary representation as a string.

    Args:
        number (int): The integer to convert to binary.

    Returns:
        str: A string representation of the binary number.

    Raises:
        TypeError: If the input is not an exact integer type.
        ValueError: If the input is a negative number.
    """
    # Strict type checking that excludes bool and float
    if type(number) is not int:
        raise TypeError("Input must be an integer")
    
    # Check if input is non-negative
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for zero
    if number == 0:
        return "0"
    
    # Convert to binary using built-in bin() and remove the '0b' prefix
    return bin(number)[2:]