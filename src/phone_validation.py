import re

def validate_phone_number(phone_number: str) -> bool:
    """
    Validate a phone number in one of three specific formats:
    1. (123) 456-7890
    2. 123-456-7890
    3. 123 456 7890

    Args:
        phone_number (str): The phone number to validate

    Returns:
        bool: True if the phone number matches one of the valid formats, False otherwise
    """
    # Regex patterns for the three specified formats
    patterns = [
        r'^\(\d{3}\)\s\d{3}-\d{4}$',   # (123) 456-7890
        r'^\d{3}-\d{3}-\d{4}$',        # 123-456-7890
        r'^\d{3}\s\d{3}\s\d{4}$'       # 123 456 7890
    ]
    
    # Check if the phone number matches any of the valid patterns
    return any(re.match(pattern, phone_number) is not None for pattern in patterns)