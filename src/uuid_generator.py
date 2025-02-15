import time
import random
import hashlib
import os

def generate_uuid():
    """
    Generate a version 4 UUID without using external libraries.
    
    Returns:
        str: A UUID in the format 8-4-4-4-12 hexadecimal characters
    """
    # Use multiple sources of entropy
    entropy_sources = [
        str(time.time()),  # Timestamp
        str(os.getpid()),  # Process ID
        str(random.randint(0, 2**64)),  # Secure random number
        ''.join(str(random.random()) for _ in range(10))  # Random float series
    ]
    
    # Combine and hash entropy sources
    combined_entropy = '|'.join(entropy_sources)
    hash_digest = hashlib.sha256(combined_entropy.encode()).hexdigest()
    
    # Prepare hex characters
    hex_chars = list(hash_digest[:32])
    
    # Enforce version 4 in third group
    hex_chars[12] = '4'
    
    # Enforce variant (10xx)
    variant_bits = ['8', '9', 'a', 'b']
    hex_chars[16] = variant_bits[int(hash_digest[16], 16) % 4]
    
    # Format into standard UUID groups
    uuid_parts = [
        ''.join(hex_chars[0:8]),    # 8 chars
        ''.join(hex_chars[8:12]),   # 4 chars
        ''.join(hex_chars[12:16]),  # 4 chars
        ''.join(hex_chars[16:20]),  # 4 chars
        ''.join(hex_chars[20:32])   # 12 chars
    ]
    
    return '-'.join(uuid_parts)