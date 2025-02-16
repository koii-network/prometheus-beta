def is_valid_ip_address(ip_string: str) -> bool:
    """
    Check if a given string is a valid IPv4 address.
    
    Args:
        ip_string (str): The string to validate as an IP address
    
    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the IP address into octets
    octets = ip_string.split('.')
    
    # A valid IP address must have exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if octet can be converted to an integer
        try:
            num = int(octet)
        except ValueError:
            return False
        
        # Check if the number is between 0 and 255
        if num < 0 or num > 255:
            return False
        
        # Check for leading zeros (except for 0 itself)
        if len(octet) > 1 and octet[0] == '0':
            return False
    
    return True