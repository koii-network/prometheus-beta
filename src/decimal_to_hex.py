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
    if not isinstance(decimal_num, int):
        raise TypeError("Input must be an integer")
    
    if decimal_num < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if decimal_num == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    hex_result = ""
    
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_result = hex_digits[remainder] + hex_result
        decimal_num //= 16
    
    return hex_result