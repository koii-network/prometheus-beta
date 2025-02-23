def hex_to_decimal(hex_string: str) -> int:
    """
    Convert a hexadecimal string to its decimal (base 10) integer representation.

    Args:
        hex_string (str): A hexadecimal string to convert. 
                          Can be prefixed with '0x' or '0X' (optional).
                          Can be uppercase or lowercase.

    Returns:
        int: The decimal representation of the hexadecimal number.

    Raises:
        ValueError: If the input is not a valid hexadecimal string.
    """
    # Remove '0x' or '0X' prefix if present
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    
    # Validate input is a valid hexadecimal string
    try:
        return int(hex_string, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")