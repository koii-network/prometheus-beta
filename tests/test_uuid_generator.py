import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_format():
    """Test that the generated UUID matches the standard format."""
    uuid = generate_uuid()
    
    # Check UUID format: 8-4-4-4-12
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid, re.IGNORECASE), f"Invalid UUID format: {uuid}"

def test_uuid_uniqueness():
    """Ensure that multiple UUID generations produce unique results."""
    uuids = set(generate_uuid() for _ in range(1000))
    assert len(uuids) == 1000, "Generated UUIDs are not unique"

def test_version_and_variant():
    """Verify version 4 and variant 1 bits are correctly set."""
    uuid = generate_uuid()
    uuid_parts = uuid.split('-')
    
    # Check version bit (4 in 3rd segment)
    assert uuid_parts[2][0] == '4', "UUID does not have version 4"
    
    # Check variant bit (8, 9, a, or b in 4th segment)
    assert uuid_parts[3][0] in '89ab', "UUID does not have correct variant"

def test_uuid_length():
    """Confirm the UUID has the correct overall length."""
    uuid = generate_uuid()
    assert len(uuid) == 36, f"Incorrect UUID length: {len(uuid)}"