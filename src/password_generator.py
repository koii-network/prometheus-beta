import random
import string

def generate_random_password(length):
    """
    Generate a random password of specified length.
    
    Args:
        length (int): The desired length of the password.
    
    Returns:
        str: A randomly generated password.
    
    Raises:
        ValueError: If length is less than 1.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Generate password by randomly selecting characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password