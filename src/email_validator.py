import re

def validate_email(email):
    """
    Validate an email address format.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Regular expression for email validation
    # This pattern checks for:
    # - Username: alphanumeric, dots, underscores, hyphens 
    # - Must have @ symbol
    # - Domain: alphanumeric, dots, hyphens
    # - Top-level domain: 2-4 alphabetic characters
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    
    # Check if email is a string
    if not isinstance(email, str):
        return False
    
    # Check if email matches the regex pattern
    return bool(re.match(email_regex, email))