import re

def validate_email(email: str) -> bool:
    """
    Validate an email address format using regex.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email format is valid, False otherwise.
    """
    # Regular expression for email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email is a string and matches the pattern
    if not isinstance(email, str):
        return False
    
    # Trim whitespace and check against regex pattern
    return bool(re.match(email_pattern, email.strip()))