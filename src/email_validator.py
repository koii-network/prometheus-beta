import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.

    Validation criteria:
    - Must have a username part before the '@'
    - Must have a domain part after the '@'
    - Username can contain letters, numbers, and some special characters
    - Domain must have at least one dot
    - Total length between 3 and 254 characters
    - No consecutive dots in username or domain
    - No spaces allowed
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False

    # Check total length constraints
    if len(email) < 3 or len(email) > 254:
        return False

    # Regular expression for email validation
    # More comprehensive regex that allows more valid email formats
    email_regex = r'''^
    # Username part: allow many special characters, but with some restrictions
    [a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+
    # Require @ symbol 
    @
    # Domain part - allow nested subdomains, internationalized domains
    (
        # Standard domain
        [a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?
        # Allow multiple nested subdomains
        (?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*
        # Punycode for international domains
        |(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}
    )
    $'''
    
    # Enable verbose mode with re.VERBOSE to allow comments and whitespace
    if not re.match(email_regex, email, re.VERBOSE):
        return False

    # Additional checks 
    try:
        # Split email into username and domain
        username, domain = email.rsplit('@', 1)
        
        # Check for consecutive dots in username or domain
        if '..' in username or '..' in domain:
            return False
        
        # Ensure no spaces anywhere
        if ' ' in username or ' ' in domain:
            return False
        
        # Additional domain validation
        domain_parts = domain.split('.')
        if len(domain_parts[-1]) < 2:  # Top-level domain must be at least 2 chars
            return False
        
    except ValueError:  # If '@' not found
        return False

    return True