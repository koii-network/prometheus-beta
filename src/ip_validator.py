def validate_ip_address(ip_string: str) -> bool:
    """
    Validate if the input string is a valid IP address in the format A.B.C.D,
    where A, B, C, and D are single digit numeric characters between 0 and 9.
    
    Args:
        ip_string (str): The IP address string to validate
    
    Returns:
        bool: True if the IP address is valid, False otherwise
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Split the string by dots
    parts = ip_string.split('.')
    
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return False
    
    # Check each part
    for part in parts:
        # Check if the part is a single digit
        if len(part) != 1:
            return False
        
        # Check if the part is a numeric character
        if not part.isdigit():
            return False
        
        # Convert to integer and check range
        num = int(part)
        if num < 0 or num > 9:
            return False
    
    return True