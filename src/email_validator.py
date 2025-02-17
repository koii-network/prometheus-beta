import re

def validate_email(email: str) -> bool:
    """
    Validate an email address format using a comprehensive regex pattern.
    
    Args:
        email (str): The email address to validate
    
    Returns:
        bool: True if the email is valid, False otherwise
    
    Validation rules:
    - Must have a username part before the @
    - Username can contain letters, numbers, dots, underscores, and hyphens
    - Must have a domain part after the @
    - Domain can contain letters, numbers, dots, and hyphens
    - Must have a top-level domain of 2-4 characters
    - Does not allow consecutive dots or special characters
    """
    # Regex pattern for email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False
    
    # Remove leading/trailing whitespace
    email = email.strip()
    
    # Check against the regex pattern
    if not re.match(email_pattern, email):
        return False
    
    # Additional checks
    # Ensure no consecutive special characters
    if re.search(r'[._%+-]{2,}', email):
        return False
    
    # Ensure domain has a valid structure
    domain = email.split('@')[1]
    if domain.startswith('.') or domain.endswith('.'):
        return False
    
    return True