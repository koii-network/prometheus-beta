import uuid

def generate_uuid() -> str:
    """
    Generate a Universally Unique Identifier (UUID).

    Returns:
        str: A string representation of a randomly generated UUID (version 4).
    """
    return str(uuid.uuid4())