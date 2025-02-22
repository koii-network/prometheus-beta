def is_valid_ip_address(ip_string: str) -> bool:
    """
    Validates if the input string is a valid IP address in the format 'A.B.C.D'
    where A, B, C, and D are single digit numeric characters between 0 and 9.
    
    Args:
        ip_string (str): The string to validate as an IP address
    
    Returns:
        bool: True if the string is a valid IP address, False otherwise
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the IP string by dots
    parts = ip_string.split('.')
    
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return False
    
    # Check each part
    for part in parts:
        # Check if part is a single digit
        if len(part) != 1:
            return False
        
        # Check if part is a digit between 0 and 9
        if not part.isdigit() or int(part) < 0 or int(part) > 9:
            return False
    
    return True