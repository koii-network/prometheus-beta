def validate_ip_address(ip_string: str) -> bool:
    """
    Validate if a given string is a valid IP address in the format A.B.C.D,
    where A, B, C, and D are single digit numeric characters between 0 and 9.

    Args:
        ip_string (str): The IP address string to validate

    Returns:
        bool: True if the IP address is valid, False otherwise
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
        # Check if each octet is exactly one character long
        if len(octet) != 1:
            return False
        
        # Check if the octet is a digit
        if not octet.isdigit():
            return False
        
        # Convert to integer and check range
        octet_value = int(octet)
        if octet_value < 0 or octet_value > 9:
            return False
    
    return True