import pytest
import re
from src.uuid_generator import generate_uuid

def test_uuid_generation():
    """Test that generate_uuid returns a valid UUID v4."""
    # Generate a UUID
    generated_uuid = generate_uuid()
    
    # Check that the generated value is a string
    assert isinstance(generated_uuid, str), "UUID should be a string"
    
    # Validate UUID format using regex for UUID v4
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, generated_uuid, re.IGNORECASE), "UUID does not match the expected format"

def test_uuid_uniqueness():
    """Test that multiple calls generate unique UUIDs."""
    # Generate multiple UUIDs
    uuids = [generate_uuid() for _ in range(100)]
    
    # Check that all UUIDs are unique
    assert len(set(uuids)) == 100, "Generated UUIDs are not unique"