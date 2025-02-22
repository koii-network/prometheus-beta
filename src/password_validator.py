import re

def validate_password(password):
    """
    Validate password based on the following complexity requirements:
    1. Minimum length of 8 characters
    2. Must contain at least one uppercase letter
    3. Must contain at least one lowercase letter
    4. Must contain at least one digit
    5. Must contain at least one special character (!@#$%^&*()_+-=)
    
    Args:
        password (str): The password to validate
    
    Returns:
        bool: True if password meets all complexity requirements, False otherwise
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
    if not re.search(r'[!@#$%^&*()_+\-=]', password):
        return False
    
    # If all checks pass, return True
    return True