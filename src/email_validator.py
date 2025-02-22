import re

def validate_email(email):
    """
    Validate an email address format.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if email is valid, False otherwise
    
    Validation criteria:
    - Must have exactly one '@' symbol
    - Local part (before '@') can contain letters, digits, and some special characters
    - Domain part (after '@') must have at least one dot
    - No whitespace allowed
    - Maximum total length of 254 characters
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False
    
    # Check total length
    if len(email) > 254:
        return False
    
    # Regular expression for email validation
    # This regex covers most common email formats
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Additional checks
    if not re.match(email_regex, email):
        return False
    
    # Split email into local and domain parts
    local_part, domain_part = email.split('@')
    
    # Additional checks for local and domain parts
    if len(local_part) > 64 or len(domain_part) > 255:
        return False
    
    # Check for consecutive dots
    if '..' in email or email.startswith('.') or email.endswith('.'):
        return False
    
    return True