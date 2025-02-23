import random
import time
import hashlib

def generate_uuid() -> str:
    """
    Generate a version 4 UUID (random) without using any UUID library.
    
    Returns:
        str: A randomly generated UUID in standard 8-4-4-4-12 format.
    """
    # Use current timestamp and random values to ensure uniqueness
    timestamp = int(time.time() * 1000)
    random_a = random.getrandbits(48)
    random_b = random.getrandbits(16)
    
    # Create a hash to add more randomness
    hash_input = f"{timestamp}{random_a}{random_b}"
    hash_obj = hashlib.md5(hash_input.encode())
    hash_hex = hash_obj.hexdigest()
    
    # Format the UUID according to version 4 specification
    # 8-4-4-4-12 hexadecimal format
    # Ensure strict adherence to the format
    uuid_parts = [
        hash_hex[:8],
        hash_hex[8:12],
        # Set the version to 4 (random) and use 3 hex chars
        f"4{hash_hex[13:15]}",
        # Set variant to 8, 9, A, or B and use 3 hex chars
        f"{int(hash_hex[16], 16) & 3 | 8:x}{hash_hex[17:19]}",
        hash_hex[20:32]
    ]
    
    return '-'.join(uuid_parts)