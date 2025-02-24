import uuid

def generate_uuid() -> str:
    """
    Generate a random Universally Unique Identifier (UUID).

    Returns:
        str: A string representation of a randomly generated UUID.

    Examples:
        >>> uuid_value = generate_uuid()
        >>> len(uuid_value) == 36  # Standard UUID length
        True
        >>> '-' in uuid_value
        True
    """
    return str(uuid.uuid4())