import re

def validate_email(email):
    """
    Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    
    Validation criteria:
    - Must have a username part before the @
    - Must have a domain part after the @
    - Username can contain letters, digits, and some special characters (., _, -)
    - Domain must have at least one dot
    - Total length constraints
    - No consecutive dots in domain
    - Strict length limits for username, domain, and top-level domain
    """
    # Check if email is a string
    if not isinstance(email, str):
        return False
    
    # Check overall email length
    if len(email) < 3 or len(email) > 254:
        return False
    
    # Check for multiple @ symbols
    if email.count('@') != 1:
        return False
    
    # Split into username and domain
    username, domain = email.split('@')
    
    # Check username length
    if len(username) > 64 or len(username) == 0:
        return False
    
    # Check for double dots and other invalid characters
    if '..' in domain or '.' not in domain:
        return False
    
    # Validate domain name
    domain_parts = domain.split('.')
    if len(domain_parts[-1]) < 2:  # Top-level domain must be at least 2 chars
        return False
    
    # Regular expression for detailed validation
    username_regex = r'^[a-zA-Z0-9._%+-]+$'
    domain_regex = r'^[a-zA-Z0-9.-]+$'
    
    # Additional checks
    if not re.match(username_regex, username):
        return False
    
    if not re.match(domain_regex, domain):
        return False
    
    return True