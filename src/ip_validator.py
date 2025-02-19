def validate_ip_address(ip_string: str) -> bool:
    """
    Validate if the input string is a valid IP address in the format 'A.B.C.D'
    where A, B, C, and D are single digit numeric characters between 0 and 9.
    
    Args:
        ip_string (str): The IP address string to validate
    
    Returns:
        bool: True if the IP address is valid, False otherwise
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Check if the IP address has exactly 3 dots
    if ip_string.count('.') != 3:
        return False
    
    # Split the IP address into octets
    octets = ip_string.split('.')
    
    # Check if we have exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if the octet is a single digit
        if len(octet) != 1:
            return False
        
        # Check if the octet is a numeric character between 0 and 9
        if not octet.isdigit():
            return False
    
    return True