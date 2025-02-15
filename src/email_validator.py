import re

def validate_email(email: str) -> bool:
    """
    Validate an email address format using regex.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if email is valid, False otherwise
    
    Validation criteria:
    - Must have a username part before @
    - Must have a domain name after @
    - Username can contain letters, numbers, dots, underscores, and hyphens
    - Domain must have at least one dot
    - Total length constraints
    """
    if not isinstance(email, str):
        return False
    
    # Trim whitespace
    email = email.strip()
    
    # Check overall length
    if len(email) < 5 or len(email) > 254:
        return False
    
    # Regex for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return re.match(pattern, email) is not None