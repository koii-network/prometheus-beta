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
    
    # Check if input is non-negative
    if decimal_num < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for 0
    if decimal_num == 0:
        return "0"
    
    # Hexadecimal digits
    hex_digits = "0123456789ABCDEF"
    
    # Convert decimal to hex
    hex_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_num = hex_digits[remainder] + hex_num
        decimal_num //= 16
    
    return hex_num