import re
import pytest
from src.uuid_generator import generate_uuid

def test_generate_uuid():
    """Test that generate_uuid returns a valid UUID."""
    # Generate multiple UUIDs to check uniqueness
    uuid1 = generate_uuid()
    uuid2 = generate_uuid()
    
    # Check that the return value is a string
    assert isinstance(uuid1, str), "UUID should be a string"
    
    # Check UUID format using regex (UUID v4 format)
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid1, re.IGNORECASE), "Invalid UUID format"
    
    # Check that generated UUIDs are unique
    assert uuid1 != uuid2, "Generated UUIDs should be unique"