def is_valid_ip_address(ip_string: str) -> bool:
    """
    Check if a given string is a valid IPv4 address.
    
    A valid IPv4 address must:
    - Consist of 4 octets separated by dots
    - Each octet must be an integer between 0 and 255
    - No leading zeros allowed (except for 0 itself)
    
    Args:
        ip_string (str): The string to validate as an IP address
    
    Returns:
        bool: True if the string is a valid IP address, False otherwise
    """
    # Check if the input is a string and not empty
    if not isinstance(ip_string, str) or not ip_string:
        return False
    
    # Split the string into octets
    octets = ip_string.split('.')
    
    # Must have exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if octet is a valid integer
        try:
            # Convert to integer, checking for invalid inputs
            num = int(octet)
            
            # Check for leading zeros (except for 0 itself)
            if len(octet) > 1 and octet[0] == '0':
                return False
            
            # Check octet is between 0 and 255
            if num < 0 or num > 255:
                return False
        
        except ValueError:
            # Not a valid integer
            return False
    
    return True