import random
import time

def generate_uuid():
    """
    Generate a version 4 UUID without using the uuid library.
    
    Returns:
        str: A randomly generated UUID in the format 
             xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx
    """
    # Timestamp component (first 8 hex characters)
    timestamp_hex = hex(int(time.time() * 1000))[2:10].zfill(8)
    
    # Generate the rest of the UUID components
    def generate_hex_char():
        return hex(random.randint(0, 15))[2:]
    
    # Generate a hex string with specified pattern
    hex_chars = [generate_hex_char() for _ in range(16)]
    
    # Set version bit (4) and variant bits
    hex_chars[6] = '4'  # version 4 UUID
    hex_chars[8] = hex(int(hex_chars[8], 16) & 3 | 8)[2:]  # variant bits
    
    # Construct UUID with proper formatting
    uuid_parts = [
        ''.join(hex_chars[0:4]),
        ''.join(hex_chars[4:6]),
        ''.join(hex_chars[6:8]),
        ''.join(hex_chars[8:10]),
        ''.join(hex_chars[10:16])
    ]
    
    return '-'.join(uuid_parts)