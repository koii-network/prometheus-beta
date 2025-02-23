def hex_to_decimal(hex_string: str) -> int:
    """
    Convert a hexadecimal string to its decimal (base 10) integer representation.
    
    Args:
        hex_string (str): A string representing a hexadecimal number.
                           Can be prefixed with '0x' or '0X' (optional).
                           Can contain uppercase or lowercase hex digits.
    
    Returns:
        int: The decimal equivalent of the input hexadecimal number.
    
    Raises:
        ValueError: If the input is not a valid hexadecimal string.
    """
    # Check for empty string
    if not hex_string:
        raise ValueError("Input cannot be empty")
    
    # Remove '0x' or '0X' prefix if present
    hex_string = hex_string.lower().replace('0x', '')
    
    # Validate that the string contains only valid hex digits
    valid_hex_chars = set('0123456789abcdef')
    if not all(char in valid_hex_chars for char in hex_string):
        raise ValueError(f"Invalid hexadecimal string: {hex_string}")
    
    # Convert to decimal using built-in int() function with base 16
    return int(hex_string, 16)