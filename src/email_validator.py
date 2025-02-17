import re

def validate_email(email):
    """
    Validate email address format using regex.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if email is valid, False otherwise
    
    Validates:
    - Presence of @ symbol
    - Username contains letters, numbers, dots, underscores, and hyphens
    - Domain contains letters, numbers, and hyphens
    - At least one dot in the domain
    """
    if not isinstance(email, str):
        return False
    
    # Regular expression for email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return bool(re.match(email_pattern, email))