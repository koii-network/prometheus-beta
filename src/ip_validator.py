def is_valid_ip_address(ip_string: str) -> bool:
    """
    Check if a given string is a valid IPv4 address.
    
    Args:
        ip_string (str): The string to validate as an IP address.
    
    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
    
    Examples:
        >>> is_valid_ip_address('192.168.0.1')
        True
        >>> is_valid_ip_address('256.0.0.1')
        False
        >>> is_valid_ip_address('192.168.0')
        False
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the IP address into octets
    octets = ip_string.split('.')
    
    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if octet is a valid integer string
        if not octet.isdigit():
            return False
        
        # Convert to integer
        try:
            num = int(octet)
        except ValueError:
            return False
        
        # Check if octet is in valid range (0-255)
        if num < 0 or num > 255:
            return False
        
        # Check for leading zeros (except for 0 itself)
        if len(octet) > 1 and octet[0] == '0':
            return False
    
    return True