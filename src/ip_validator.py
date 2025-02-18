def is_valid_ip_address(ip_string):
    """
    Check if a given string is a valid IPv4 address.
    
    Args:
        ip_string (str): The string to validate as an IP address.
    
    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
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
        # Check if octet is numeric
        if not octet.isdigit():
            return False
        
        # Convert to integer
        try:
            octet_value = int(octet)
        except ValueError:
            return False
        
        # Check range (0-255)
        if octet_value < 0 or octet_value > 255:
            return False
        
        # Ensure no leading zeros for non-zero numbers
        if len(octet) > 1 and octet[0] == '0':
            return False
    
    return True