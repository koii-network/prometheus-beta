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
    # This regex follows RFC 5322 standard with some practical constraints
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email is a string
    if not isinstance(email, str):
        return False
    
    # Check email against the regex pattern
    if re.match(email_regex, email):
        return True
    
    return False