import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.

    Validates an email address based on RFC 5322 standard with some practical constraints:
    - Must have a local part and domain part separated by @
    - Local part can contain letters, digits, and some special characters
    - Domain must have at least one dot
    - Total length should be reasonable
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False

    # Check total length (RFC 5322 suggests max 254 characters)
    if len(email) > 254:
        return False

    # Regular expression for email validation
    # This regex follows most common email format rules
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the regex pattern
    if not re.match(email_regex, email):
        return False

    # Additional checks
    local_part, domain = email.split('@')
    
    # Check local part length (local part max 64 characters)
    if len(local_part) > 64:
        return False

    # Check domain part (must have at least one dot)
    if '.' not in domain:
        return False

    return True