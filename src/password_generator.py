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
        ValueError: If length is less than 4 to ensure password complexity.
    """
    if not isinstance(length, int):
        raise TypeError("Length must be an integer")
    
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]
    
    # Fill the rest of the password with random characters
    remaining_length = length - 4
    all_characters = lowercase + uppercase + digits + punctuation
    password.extend(random.choice(all_characters) for _ in range(remaining_length))
    
    # Shuffle the password to randomize character positions
    random.shuffle(password)
    
    return ''.join(password)