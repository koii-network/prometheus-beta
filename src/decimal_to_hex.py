def decimal_to_hex(decimal_num):
    """
    Convert a decimal number to its hexadecimal representation.

    Args:
        decimal_num (int): The decimal number to convert.

    Returns:
        str: The hexadecimal representation of the input number.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """
    # Check if input is an integer
    if not isinstance(decimal_num, int):
        raise TypeError("Input must be an integer")
    
    # Check for negative numbers
    if decimal_num < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for zero
    if decimal_num == 0:
        return "0"
    
    # Hex conversion using built-in hex() function and removing the '0x' prefix
    return hex(decimal_num)[2:].upper()