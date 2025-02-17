import re

def validate_email(email: str) -> bool:
    """
    Validate an email address format using a comprehensive regex pattern.
    
    Args:
        email (str): The email address to validate
    
    Returns:
        bool: True if the email format is valid, False otherwise
    """
    # Regular expression for email validation
    # Follows RFC 5322 standards with some practical constraints
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email is a string and matches the regex pattern
    if not isinstance(email, str):
        return False
    
    # Strip whitespace and validate
    email = email.strip()
    
    # Check for empty string
    if not email:
        return False
    
    # Validate using regex
    return re.match(email_regex, email) is not None