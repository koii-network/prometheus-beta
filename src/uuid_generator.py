import random
import time

def generate_uuid() -> str:
    """
    Generate a version 4 UUID (Universally Unique Identifier) without using external libraries.
    
    The UUID is generated using a combination of:
    - Current timestamp (high precision)
    - Random bytes
    - Formatted according to UUID v4 standard
    
    Returns:
        str: A UUID in the format '8-4-4-4-12' hexadecimal string
    """
    # Get current timestamp (high precision)
    timestamp = int(time.time() * 1000000)
    
    # Generate random bytes
    random_bytes = [random.randint(0, 255) for _ in range(16)]
    
    # Apply version 4 UUID variant bits
    random_bytes[6] = (random_bytes[6] & 0x0F) | 0x40  # version 4
    random_bytes[8] = (random_bytes[8] & 0x3F) | 0x80  # variant 1
    
    # Convert to UUID string format
    hex_chars = [f'{b:02x}' for b in random_bytes]
    uuid_str = (
        f"{''.join(hex_chars[0:4])}-"
        f"{''.join(hex_chars[4:6])}-"
        f"{''.join(hex_chars[6:8])}-"
        f"{''.join(hex_chars[8:10])}-"
        f"{''.join(hex_chars[10:16])}"
    )
    
    return uuid_str