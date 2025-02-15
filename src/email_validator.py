import re

def validate_email(email: str) -> bool:
    """
    Validate an email address format.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Regular expression for email validation
    # Checks for:
    # - Username: letters, numbers, and some special characters
    # - Requires @ symbol
    # - Domain: letters, numbers, hyphens
    # - Top-level domain: 2-4 letters
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    
    # Check if email is a string and matches the regex pattern
    if not isinstance(email, str):
        return False
    
    return bool(re.match(email_regex, email))