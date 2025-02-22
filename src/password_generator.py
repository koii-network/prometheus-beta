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
        raise ValueError("Password length must be at least 1 character")
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password with random characters
    remaining_length = length - 4
    all_chars = lowercase + uppercase + digits + special_chars
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle the password to randomize character positions
    random.shuffle(password)
    
    return ''.join(password)