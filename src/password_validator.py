import re

def validate_password(password):
    """
    Validate a password based on the following complexity requirements:
    - Minimum length of 8 characters
    - Must contain at least one uppercase letter
    - Must contain at least one lowercase letter
    - Must contain at least one digit
    - Must contain at least one special character from !@#$%^&*()

    Args:
        password (str): The password to validate

    Returns:
        bool: True if the password meets all complexity requirements, False otherwise
    """
    # Check if password is None or not a string
    if not isinstance(password, str):
        return False

    # Check minimum length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()]', password):
        return False

    # If all checks pass, return True
    return True