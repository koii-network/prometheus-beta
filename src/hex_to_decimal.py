def hex_to_decimal(hex_string):
    """
    Convert a hexadecimal string to its decimal (integer) representation.
    
    Args:
        hex_string (str): A hexadecimal string (can have optional '0x' prefix)
    
    Returns:
        int: Decimal representation of the hexadecimal number
    
    Raises:
        ValueError: If the input is not a valid hexadecimal string
    """
    try:
        # Remove '0x' or '0X' prefix if present
        if hex_string.startswith(('0x', '0X')):
            hex_string = hex_string[2:]
        
        # Convert hex to decimal using built-in int() function with base 16
        return int(hex_string, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")