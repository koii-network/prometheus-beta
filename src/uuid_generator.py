import random
import time
import os

def generate_uuid():
    """
    Generate a Version 4 UUID without using built-in UUID libraries.
    
    This implementation creates a pseudo-random UUID that follows the RFC 4122 standard 
    for version 4 UUIDs, with randomness derived from system time and cryptographic sources.
    
    Returns:
        str: A string representation of a UUID in standard 8-4-4-4-12 format
    """
    # Use os.urandom for cryptographically strong randomness
    # If unavailable, fallback to system time and random
    try:
        random_bytes = list(os.urandom(16))
    except NotImplementedError:
        # Fallback method with more entropy
        random.seed(time.time_ns())
        random_bytes = [random.randint(0, 255) for _ in range(16)]
    
    # Explicitly set version 4 at 7th byte (13th hex character)
    # Clear the top 4 bits and set to 0100 (version 4)
    random_bytes[6] = (random_bytes[6] & 0x0F) | 0x40
    
    # Set variant (RFC 4122): set top two bits to 10
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