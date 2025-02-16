import random
import string

def generate_random_password(length: int) -> str:
    """
    Generate a random password of the specified length.
    
    Args:
        length (int): The desired length of the password.
    
    Returns:
        str: A randomly generated password.
    
    Raises:
        ValueError: If the length is less than 1.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase + uppercase + digits + punctuation
    
    # Generate password by randomly selecting characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password