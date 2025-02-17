import uuid

def generate_uuid() -> str:
    """
    Generate a Universally Unique Identifier (UUID).
    
    Returns:
        str: A randomly generated UUID as a string.
    """
    return str(uuid.uuid4())