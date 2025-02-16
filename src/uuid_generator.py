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
    timestamp = int(time.time() * 1000)
    random_bytes = os.urandom(10) if hasattr(os, 'urandom') else os.getrandom(10)
    
    # Generate hex representation
    hex_timestamp = hex(timestamp)[2:].zfill(12)
    hex_random = ''.join([f'{byte:02x}' for byte in random_bytes])
    
    # Construct UUID parts with version 4 variant
    parts = [
        hex_timestamp[:8],  # 8 chars from timestamp
        hex_random[:4],     # 4 random chars
        f'4{hex_random[4:5]}',  # Version 4 UUID (starts with 4)
        f'{int(hex_random[5:6], 16) & 0x3 | 0x8:x}{hex_random[6:8]}',  # Variant and random
        hex_random[8:20]   # Last 12 chars
    ]
    
    return '-'.join(parts)