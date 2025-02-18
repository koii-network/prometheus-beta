def hex_to_decimal(hex_string):
    """
    Convert a hexadecimal string to its decimal (integer) equivalent.
    
    Args:
        hex_string (str): A string representing a hexadecimal number.
                           Can be prefixed with '0x' or '0X' (optional).
    
    Returns:
        int: The decimal representation of the hexadecimal number.
    
    Raises:
        ValueError: If the input is not a valid hexadecimal string.
    """
    # Remove '0x' or '0X' prefix if present
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    
    try:
        # Convert hexadecimal string to decimal integer
        return int(hex_string, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")