def decimal_to_hex(decimal_num):
    """
    Convert a decimal number to its hexadecimal representation.
    
    Args:
        decimal_num (int): The decimal number to convert.
    
    Returns:
        str: The hexadecimal representation of the decimal number.
    
    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.
    """
    # Check input type
    if not isinstance(decimal_num, int):
        raise TypeError("Input must be an integer")
    
    # Check for negative numbers
    if decimal_num < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for zero
    if decimal_num == 0:
        return "0"
    
    # Hexadecimal conversion
    hex_digits = "0123456789ABCDEF"
    hex_result = []
    
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_result.insert(0, hex_digits[remainder])
        decimal_num //= 16
    
    return ''.join(hex_result)