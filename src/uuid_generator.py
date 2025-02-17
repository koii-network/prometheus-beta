import uuid

def generate_uuid() -> str:
    """
    Generate a universally unique identifier (UUID).
    
    Returns:
        str: A randomly generated UUID as a string.
    """
    return str(uuid.uuid4())