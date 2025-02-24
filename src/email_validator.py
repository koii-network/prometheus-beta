import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.

    Validation Rules:
    - Must have a username part before the @ symbol
    - Must have a domain part after the @ symbol
    - Username can contain letters, numbers, dots, underscores, and hyphens
    - Domain must have at least one dot
    - Total length must be between 3 and 254 characters
    - No consecutive dots in username or domain
    - Cannot start or end with a dot
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False

    # Check total length
    if len(email) < 3 or len(email) > 254:
        return False

    # Regular expression for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Additional checks
    if not re.match(email_regex, email):
        return False

    # Prevent consecutive dots
    if '..' in email:
        return False

    # Cannot start or end with a dot in local or domain part
    local_part, domain_part = email.split('@')
    if local_part.startswith('.') or local_part.endswith('.') or \
       domain_part.startswith('.') or domain_part.endswith('.'):
        return False

    return True