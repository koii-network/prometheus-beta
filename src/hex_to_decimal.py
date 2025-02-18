def hex_to_decimal(hex_string: str) -> int:
    """
    Convert a hexadecimal string to its decimal (base 10) equivalent.
    
    Args:
        hex_string (str): A hexadecimal string representation (can include '0x' prefix)
    
    Returns:
        int: The decimal equivalent of the hex number
    
    Raises:
        ValueError: If the input is not a valid hexadecimal string
    """
    # Remove '0x' or '0X' prefix if present
    hex_string = hex_string.lower().replace('0x', '')
    
    try:
        return int(hex_string, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")