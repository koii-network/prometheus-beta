import re

def validate_phone_number(phone_number: str) -> bool:
    """
    Validate phone number in three specific formats:
    1. (123) 456-7890
    2. 123-456-7890
    3. 123 456 7890
    
    Args:
        phone_number (str): Phone number to validate
    
    Returns:
        bool: True if phone number matches one of the valid formats, False otherwise
    """
    # Regular expression patterns for the three valid phone number formats
    patterns = [
        r'^\(\d{3}\)\s\d{3}-\d{4}$',  # (123) 456-7890
        r'^\d{3}-\d{3}-\d{4}$',        # 123-456-7890
        r'^\d{3}\s\d{3}\s\d{4}$'        # 123 456 7890
    ]
    
    # Check if phone number matches any of the patterns
    return any(re.match(pattern, phone_number) for pattern in patterns)