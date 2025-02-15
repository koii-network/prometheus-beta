import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    
    Validation rules:
    - Must have a username part before the @
    - Must have a domain part after the @
    - Username can contain letters, numbers, periods, underscores, and hyphens
    - Domain must have at least one dot
    - Total length should be between 3 and 254 characters
    """
    # Check overall email length
    if not email or len(email) < 3 or len(email) > 254:
        return False
    
    # Regular expression for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the regex pattern
    return re.match(email_regex, email) is not None