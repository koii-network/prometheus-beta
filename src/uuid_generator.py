import time
import random

def generate_uuid():
    """
    Generate a version 4 UUID without using external libraries.
    
    Returns:
        str: A UUID in the standard 8-4-4-4-12 format
    """
    # Current timestamp
    timestamp = int(time.time() * 1000)
    
    # Use random for generating UUID components
    segments = [
        # First segment: 8 hex characters of randomness/timestamp
        f"{timestamp & 0xFFFFFFFF:08x}",
        
        # Next 3 segments: 4 hex characters each, with version 4 (random) specifics
        f"{random.randint(0, 0xFFFF):04x}",
        f"{(random.randint(0, 0xFFF) & 0x0FFF) | 0x4000:04x}",  # Version 4
        f"{(random.randint(0, 0xFFFF) & 0x3FFF) | 0x8000:04x}",  # Variant 1
        
        # Last segment: 12 hex characters of random data
        f"{random.randint(0, 0xFFFFFFFFFFFF):012x}"
    ]
    
    return "-".join(segments)