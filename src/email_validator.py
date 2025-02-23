import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.

    Validation criteria:
    - Must have a username part before the @
    - Must have a domain name after the @
    - Username can contain letters, numbers, dots, underscores, and hyphens
    - Domain must have at least one dot
    - Total length should be between 3 and 254 characters
    - Cannot start or end with a dot in username
    - Cannot have consecutive dots
    """
    # Check overall length constraints
    if not email or len(email) < 3 or len(email) > 254:
        return False

    # Split email into username and domain
    try:
        username, domain = email.split('@')
    except ValueError:
        return False
    
    # Validate username
    if '..' in username or username.startswith('.') or username.endswith('.'):
        return False
    
    # Validate domain
    if not domain or '..' in domain or domain.startswith('.') or domain.startswith('-') or domain.endswith('-'):
        return False
    
    # Regular expression for email validation
    # Stricter regex to prevent hyphens/dots at start/end of domain parts
    email_regex = r'^[a-zA-Z0-9._%+-]+[a-zA-Z0-9]@[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$'
    
    # Additional checks to handle edge cases
    if not re.match(email_regex, email):
        return False
    
    # Ensure domain has at least one dot and valid TLD
    domain_parts = domain.split('.')
    if len(domain_parts[-1]) < 2:  # TLD must be at least 2 characters
        return False
    
    return True