import random
import string

def generate_verification_code(used_codes=None):
    """
    Generate a unique 6-digit verification code.
    
    Args:
        used_codes (set, optional): A set of previously used codes to ensure uniqueness.
    
    Returns:
        str: A unique 6-digit verification code.
    
    Raises:
        ValueError: If unable to generate a unique code after multiple attempts.
    """
    if used_codes is None:
        used_codes = set()
    
    max_attempts = 100
    
    for _ in range(max_attempts):
        # Generate a 6-digit code with random digits
        code = ''.join(random.choices(string.digits, k=6))
        
        # Check if the code is unique
        if code not in used_codes:
            used_codes.add(code)
            return code
    
    raise ValueError("Unable to generate a unique verification code")

def validate_verification_code(code):
    """
    Validate a verification code.
    
    Args:
        code (str): The verification code to validate.
    
    Returns:
        bool: True if the code is valid, False otherwise.
    """
    # Check if the code is a 6-digit string containing only numbers
    return (
        isinstance(code, str) and 
        len(code) == 6 and 
        code.isdigit()
    )