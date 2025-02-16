import re

def validate_email(email):
    """
    Validate an email address format.
    
    Args:
        email (str): The email address to validate
    
    Returns:
        bool: True if the email is valid, False otherwise
    
    Validates email based on RFC 5322 standard with some practical constraints:
    - Must have a username and domain
    - Username can contain letters, numbers, and some special characters
    - Domain must have at least one dot
    - Top-level domain must be 2-4 characters
    """
    if not isinstance(email, str):
        return False
    
    # Regular expression for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    
    return re.match(email_regex, email) is not None