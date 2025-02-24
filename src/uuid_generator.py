import random
import time
import hashlib

def generate_uuid():
    """
    Generate a Version 4 UUID without using built-in UUID libraries.
    
    This implementation creates a pseudo-random UUID that follows the RFC 4122 standard 
    for version 4 UUIDs, with randomness derived from system time and random sources.
    
    Returns:
        str: A string representation of a UUID in standard 8-4-4-4-12 format
    """
    # Get current timestamp for added entropy
    timestamp = int(time.time() * 1000)
    
    # Use system's randomness and timestamp to create entropy
    random.seed(timestamp)
    
    # Generate 16 random bytes
    random_bytes = [random.randint(0, 255) for _ in range(16)]
    
    # Set version (4) and variant bits as per RFC 4122
    # Version 4 UUID has 4 in the first 4 bits of the 7th byte
    random_bytes[6] = (random_bytes[6] & 0x0F) | 0x40
    
    # Set variant bits (2 most significant bits of 9th byte)
    random_bytes[8] = (random_bytes[8] & 0x3F) | 0x80
    
    # Convert to hex and format in standard UUID representation
    hex_bytes = [f'{b:02x}' for b in random_bytes]
    
    # Format as standard UUID: 8-4-4-4-12 format
    uuid_str = ''.join([
        ''.join(hex_bytes[0:4]),
        '-',
        ''.join(hex_bytes[4:6]),
        '-',
        ''.join(hex_bytes[6:8]),
        '-',
        ''.join(hex_bytes[8:10]),
        '-',
        ''.join(hex_bytes[10:16])
    ])
    
    return uuid_str