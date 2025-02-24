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
    - Requires valid top-level domain
    - Domain parts cannot start or end with hyphen
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False

    # Check total length constraints
    if len(email) < 3 or len(email) > 254:
        return False

    # Check basic email format
    try:
        # Split into username and domain
        username, domain = email.rsplit('@', 1)
        
        # Validate username
        if not username or len(username) > 64:
            return False
        
        # Validate domain
        if not domain or domain.startswith('.') or domain.endswith('.'):
            return False
        
        # Domain parts cannot start or end with hyphen
        domain_parts = domain.split('.')
        if any(part.startswith('-') or part.endswith('-') for part in domain_parts):
            return False
        
        # Check for single dot and valid TLD
        if len(domain_parts) < 2 or len(domain_parts[-1]) < 2:
            return False
        
        # Additional checks for username and domain
        if '..' in username or '..' in domain:
            return False
        
        # No spaces
        if ' ' in username or ' ' in domain:
            return False
        
    except ValueError:
        return False

    # Regex for more nuanced validation
    # Allow a wide range of valid characters while preventing most invalid formats
    email_regex = r'''
    ^
    # Username allows many characters, but with some restrictions
    [a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+
    # Require @ symbol
    @
    # Domain allows standard domain names and punycode
    (
        # Standard domain with nested subdomains
        [a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?
        (?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*
        |
        # Internationalized domain names (Punycode)
        (?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}
    )
    $'''
    
    return bool(re.match(email_regex, email, re.VERBOSE))