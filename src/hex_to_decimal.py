def hex_to_decimal(hex_string):
    """
    Convert a hexadecimal string to its decimal (integer) representation.
    
    Args:
        hex_string (str): A hexadecimal string (can be prefixed with '0x' or '0X').
    
    Returns:
        int: The decimal representation of the hexadecimal string.
    
    Raises:
        ValueError: If the input is not a valid hexadecimal string.
    """
    # Remove '0x' or '0X' prefix if present
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    
    # Validate that the string contains only valid hex characters
    valid_hex_chars = set('0123456789abcdefABCDEF')
    if not all(char in valid_hex_chars for char in hex_string):
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")
    
    # Convert to decimal using built-in int() function with base 16
    return int(hex_string, 16)