def is_valid_ip_address(ip_string: str) -> bool:
    """
    Check if a given string is a valid IPv4 address.
    
    A valid IPv4 address must:
    - Consist of 4 octets separated by dots
    - Each octet must be an integer between 0 and 255
    - No leading zeros (except 0 itself)
    - No non-numeric characters except dots
    
    Args:
        ip_string (str): The string to validate as an IP address
    
    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise
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
        # Check if octet is empty
        if not octet:
            return False
        
        # Check for leading zeros (except single 0)
        if len(octet) > 1 and octet[0] == '0':
            return False
        
        # Check if octet contains only digits
        if not octet.isdigit():
            return False
        
        # Convert to integer and check range
        try:
            octet_value = int(octet)
            if octet_value < 0 or octet_value > 255:
                return False
        except ValueError:
            return False
    
    return True