import re

def validate_email(email):
    """
    Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    
    Validation criteria:
    - Must have a username part before the @
    - Must have a domain part after the @
    - Username can contain letters, digits, and some special characters (., _, -)
    - Domain must have at least one dot
    - Total length constraints
    """
    # Check if email is a string
    if not isinstance(email, str):
        return False
    
    # Check overall email length
    if len(email) < 3 or len(email) > 254:
        return False
    
    # Regular expression for email validation
    # Breakdown of regex:
    # ^             : Start of string
    # [a-zA-Z0-9._%+-]+ : Username can have letters, digits, and some special chars
    # @             : Mandatory @ symbol
    # [a-zA-Z0-9.-]+  : Domain name 
    # \.            : Mandatory dot in domain
    # [a-zA-Z]{2,}  : Top-level domain (at least 2 letters)
    # $             : End of string
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return bool(re.match(email_regex, email))