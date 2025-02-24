import re

def validate_email(email):
    """
    Validate an email address format.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    
    Validates email format based on RFC 5322 standards with practical constraints:
    - Must have a local part (before @)
    - Must have a domain part (after @)
    - Allows uppercase and lowercase letters
    - Allows digits, some special characters in local part
    - Requires a valid domain with at least one dot
    - Maximum total length of 254 characters
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False
    
    # Check total email length (RFC 5322 standard max length)
    if len(email) > 254:
        return False
    
    # Regular expression for email validation
    # This regex provides a comprehensive email format check
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z]{2,})+$'
    
    # Check for consecutive dots in domain
    if '..' in email:
        return False
    
    # Basic pattern match
    if not re.match(email_regex, email):
        return False
    
    # Custom length check for domain and local part
    try:
        local_part, domain = email.split('@')
        if len(local_part) > 64 or len(domain) > 190:
            return False
    except ValueError:
        return False
    
    return True