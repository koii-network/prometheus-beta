import random
import time

def generate_uuid():
    """
    Generate a version 4 UUID without using the uuid library.
    
    Returns:
        str: A randomly generated UUID in the format 
             xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
    """
    def generate_hex_char():
        return hex(random.randint(0, 15))[2:]
    
    # Generate a hex string with specified pattern
    hex_chars = [generate_hex_char() for _ in range(32)]
    
    # Set version bit (4) and variant bits
    hex_chars[12] = '4'  # version 4 UUID
    hex_chars[16] = hex(int(hex_chars[16], 16) & 3 | 8)[2:]  # variant bits
    
    # Construct UUID with proper formatting
    uuid_parts = [
        ''.join(hex_chars[0:8]),
        ''.join(hex_chars[8:12]),
        ''.join(hex_chars[12:16]),
        ''.join(hex_chars[16:20]),
        ''.join(hex_chars[20:32])
    ]
    
    return '-'.join(uuid_parts)