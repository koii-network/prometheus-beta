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
    random_a = random.getrandbits(128)
    
    # Create a hash to add more randomness
    hash_input = f"{timestamp}{random_a}"
    hash_obj = hashlib.md5(hash_input.encode())
    hash_hex = hash_obj.hexdigest()
    
    # Format the UUID according to version 4 specification
    # 8-4-4-4-12 hexadecimal format
    uuid_parts = [
        hash_hex[:8],  # 8 chars
        hash_hex[8:12],  # 4 chars
        f"4{hash_hex[12:15]}",  # version 4 + 3 chars
        f"{int(hash_hex[16], 16) & 3 | 8:x}{hash_hex[17:19]}",  # variant + 3 chars
        hash_hex[20:32]  # 12 chars
    ]
    
    return '-'.join(uuid_parts)