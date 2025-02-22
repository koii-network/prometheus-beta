import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_generation():
    """Test UUID generation meets basic requirements."""
    uuid = generate_uuid()
    
    # Check UUID format: 8-4-4-4-12 hexadecimal characters
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid), f"Invalid UUID format: {uuid}"

def test_uuid_uniqueness():
    """Test that multiple UUIDs are unique."""
    uuids = {generate_uuid() for _ in range(100)}
    assert len(uuids) == 100, "UUIDs are not unique"

def test_uuid_version():
    """Test that UUID follows version 4 specification."""
    uuid = generate_uuid()
    # Check version 4 specification: 4 at 13th character position (0-based index)
    assert uuid[14] == '4', "Not a version 4 UUID"

def test_uuid_variant():
    """Test that UUID follows variant specification."""
    uuid = generate_uuid()
    # Check variant specification: 8, 9, a, or b at 16th character position (0-based index)
    assert uuid[19] in '89ab', "Invalid UUID variant"