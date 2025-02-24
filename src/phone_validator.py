import re

def validate_phone_number(phone_number: str) -> bool:
    """
    Validate a phone number against three specific formats:
    1. (123) 456-7890
    2. 123-456-7890
    3. 123 456 7890

    Args:
        phone_number (str): The phone number to validate

    Returns:
        bool: True if the phone number matches one of the valid formats, False otherwise
    
    Raises:
        TypeError: If input is not a string
    """
    # Check if input is None or not a string
    if phone_number is None or not isinstance(phone_number, str):
        raise TypeError("Input must be a string")
    
    # Regular expression patterns for the three specified formats
    patterns = [
        r'^\(\d{3}\)\s\d{3}-\d{4}$',   # (123) 456-7890
        r'^\d{3}-\d{3}-\d{4}$',        # 123-456-7890
        r'^\d{3}\s\d{3}\s\d{4}$'       # 123 456 7890
    ]
    
    # Remove any whitespace from the input
    phone_number = phone_number.strip()
    
    # Check if the phone number matches any of the patterns
    return any(re.match(pattern, phone_number) for pattern in patterns)