import re
import pytest
from src.uuid_generator import generate_uuid

def test_generate_uuid():
    """
    Test UUID generation functionality.
    """
    # Generate a UUID
    generated_uuid = generate_uuid()
    
    # Check that the generated UUID is a string
    assert isinstance(generated_uuid, str), "UUID should be a string"
    
    # Validate UUID format (v4 UUID regex pattern)
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, generated_uuid, re.IGNORECASE), "UUID does not match expected format"

def test_uuid_uniqueness():
    """
    Test that multiple generated UUIDs are unique.
    """
    # Generate multiple UUIDs
    uuids = [generate_uuid() for _ in range(1000)]
    
    # Check that all UUIDs are unique
    assert len(set(uuids)) == len(uuids), "Generated UUIDs should be unique"