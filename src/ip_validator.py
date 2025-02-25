def is_valid_ip_address(ip_string: str) -> bool:
    """
    Validate if a given string is a valid IPv4 address.
    
    Args:
        ip_string (str): The string to validate as an IP address
    
    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise
    """
    # Split the string into octets
    try:
        octets = ip_string.split('.')
        
        # Check if there are exactly 4 octets
        if len(octets) != 4:
            return False
        
        # Check each octet
        for octet in octets:
            # Check if octet is a valid integer
            try:
                num = int(octet)
            except ValueError:
                return False
            
            # Check if number is within valid range (0-255)
            if num < 0 or num > 255:
                return False
            
            # Reject leading zeros (except for zero itself)
            if len(octet) > 1 and octet[0] == '0':
                return False
        
        return True
    
    except Exception:
        return False