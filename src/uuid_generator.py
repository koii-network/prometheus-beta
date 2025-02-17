import uuid

def generate_uuid() -> str:
    """
    Generate a Universally Unique Identifier (UUID).
    
    Returns:
        str: A unique UUID in standard string representation.
    """
    return str(uuid.uuid4())