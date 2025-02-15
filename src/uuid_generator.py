import uuid

def generate_uuid() -> str:
    """
    Generate a Universally Unique Identifier (UUID).
    
    Returns:
        str: A string representation of a randomly generated UUID.
    """
    return str(uuid.uuid4())