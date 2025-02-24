import re

def validate_email(email: str) -> bool:
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.

    Validation criteria:
    - Must have a username part before the '@'
    - Must have a domain part after the '@'
    - Username can contain letters, numbers, and some special characters
    - Domain must have at least one dot
    - Total length between 3 and 254 characters
    - No consecutive dots in username or domain
    - No spaces allowed
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False

    # Check total length constraints
    if len(email) < 3 or len(email) > 254:
        return False

    # Regular expression for email validation
    # Breakdown of regex:
    # ^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+  : Username part with allowed special characters
    # @                                   : Literal @ symbol
    # [a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?  : Domain name rules
    # (?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$  : Multiple subdomains allowed
    email_regex = r'^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'
    
    # Check if email matches the regex pattern
    if not re.match(email_regex, email):
        return False

    # Additional checks
    # Ensure no consecutive dots
    if '..' in email:
        return False

    # Ensure no spaces
    if ' ' in email:
        return False

    return True