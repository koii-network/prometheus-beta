import os
import time
import random

def generate_uuid():
    """
    Generate a version 4 UUID (random) without using external libraries.
    
    Returns:
        str: A UUID in the standard 8-4-4-4-12 format (e.g., '550e8400-e29b-4214-a536-123456789012')
    """
    # Use current timestamp and random bytes for uniqueness
    random_bytes = os.urandom(16) if hasattr(os, 'urandom') else os.getrandom(16)
    
    # Modify specific bytes to create a version 4 UUID with the right variant
    random_bytes = bytearray(random_bytes)
    random_bytes[6] = (random_bytes[6] & 0x0f) | 0x40  # Version 4
    random_bytes[8] = (random_bytes[8] & 0x3f) | 0x80  # Variant 10
    
    # Convert to hex and format UUID
    hex_uuid = ''.join([f'{b:02x}' for b in random_bytes])
    return f'{hex_uuid[:8]}-{hex_uuid[8:12]}-{hex_uuid[12:16]}-{hex_uuid[16:20]}-{hex_uuid[20:]}'