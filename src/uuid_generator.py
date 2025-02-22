import time
import random

def generate_uuid():
    """
    Generate a version 4 UUID without using external libraries.
    
    Returns:
        str: A UUID in the format: 8-4-4-4-12 hexadecimal characters
    """
    # Get current timestamp and use as part of randomness
    timestamp = int(time.time() * 1000)
    random.seed(timestamp)
    
    # Generate random hexadecimal parts
    parts = [
        # 8 characters
        ''.join(random.choice('0123456789abcdef') for _ in range(8)),
        # 4 characters
        ''.join(random.choice('0123456789abcdef') for _ in range(4)),
        # 4 characters with version 4 modification
        '4' + ''.join(random.choice('0123456789abcdef') for _ in range(3)),
        # 4 characters with variant modification (starts with 8, 9, a, or b)
        random.choice('89ab') + ''.join(random.choice('0123456789abcdef') for _ in range(3)),
        # 12 characters
        ''.join(random.choice('0123456789abcdef') for _ in range(12))
    ]
    
    return '-'.join(parts)