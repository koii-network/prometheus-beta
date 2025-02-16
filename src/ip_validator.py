def is_valid_ip_address(ip_string: str) -> bool:
    """
    Validate if the given string is a valid IPv4 address.
    
    Args:
        ip_string (str): The string to validate as an IP address.
    
    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the string into octets
    octets = ip_string.split('.')
    
    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if octet is a valid integer between 0 and 255
        try:
            # Convert to integer and check range
            num = int(octet)
            
            # Check for leading zeros (except for zero itself)
            if len(octet) > 1 and octet[0] == '0':
                return False
            
            # Check range
            if num < 0 or num > 255:
                return False
        except ValueError:
            # If conversion to integer fails
            return False
    
    return True