import time
import random

def generate_uuid():
    """
    Generate a version 4 UUID without using external libraries.
    
    Returns:
        str: A UUID in the format 8-4-4-4-12 hexadecimal characters
    """
    # Get current timestamp for some randomness
    timestamp = int(time.time() * 1000)
    random.seed(timestamp)
    
    # Generate 32 random hexadecimal characters
    hex_chars = '0123456789abcdef'
    uuid_chars = [random.choice(hex_chars) for _ in range(32)]
    
    # Apply UUID v4 variant and version bits
    # Set the variant (bits 6-7 of 8th hex character) to 0b10
    uuid_chars[16] = hex_chars[(int(uuid_chars[16], 16) & 0x3) | 0x8]
    
    # Set the version (bits 6-7 of 6th hex character) to 0b0100 (version 4)
    uuid_chars[14] = hex_chars[(int(uuid_chars[14], 16) & 0x3) | 0x4]
    
    # Format into standard UUID groups
    uuid_format = [8, 4, 4, 4, 12]
    formatted_uuid = []
    start = 0
    
    for length in uuid_format:
        formatted_uuid.append(''.join(uuid_chars[start:start+length]))
        start += length
    
    return '-'.join(formatted_uuid)