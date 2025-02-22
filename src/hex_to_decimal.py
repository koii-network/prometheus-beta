def hex_to_decimal(hex_string: str) -> int:
    """
    Convert a hexadecimal string to its decimal (base 10) integer equivalent.
    
    Args:
        hex_string (str): A hexadecimal string (can include '0x' prefix or not)
    
    Returns:
        int: The decimal equivalent of the input hexadecimal string
    
    Raises:
        ValueError: If the input is not a valid hexadecimal string
    """
    # Remove '0x' prefix if present (case-insensitive)
    hex_string = hex_string.lower().replace('0x', '')
    
    try:
        # Use built-in int() function with base 16 for conversion
        return int(hex_string, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")