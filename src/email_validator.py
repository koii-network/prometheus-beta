import re

def validate_email(email):
    """
    Validate an email address format.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    
    Validation criteria:
    - Must have a username part before the @
    - Must have a domain name after the @
    - Username can contain letters, numbers, dots, underscores, and hyphens
    - Domain must have at least one dot
    - No consecutive dots in username or domain
    - Total length constraints
    """
    if not isinstance(email, str):
        return False
    
    # Regular expression for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check overall regex pattern
    if not re.match(email_regex, email):
        return False
    
    # Additional checks
    # Length constraints
    if len(email) > 254:
        return False
    
    # Split into username and domain
    username, domain = email.split('@')
    
    # Username length check
    if len(username) > 64:
        return False
    
    # No consecutive dots
    if '..' in username or '..' in domain:
        return False
    
    return True