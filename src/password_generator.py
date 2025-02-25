import secrets
import string

def generate_random_password(length):
    """
    Generate a secure random password of the specified length.

    Args:
        length (int): The desired length of the password.
    
    Returns:
        str: A randomly generated password.
    
    Raises:
        ValueError: If the length is less than 1.
    """
    # Validate input
    if not isinstance(length, int):
        raise TypeError("Password length must be an integer")
    
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase + uppercase + digits + punctuation
    
    # Generate password using cryptographically secure random selection
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    
    return password