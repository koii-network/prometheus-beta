import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_generation():
    """Test basic UUID generation characteristics."""
    uuid = generate_uuid()
    
    # Check overall format
    assert re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', uuid), \
        "UUID does not match expected format"

def test_uuid_uniqueness():
    """Ensure multiple generated UUIDs are unique."""
    uuids = set(generate_uuid() for _ in range(1000))
    assert len(uuids) == 1000, "Generated UUIDs are not unique"

def test_uuid_version():
    """Verify the version and variant bits are correct."""
    uuid = generate_uuid()
    
    # Check version bit (should be 4 in 3rd group)
    version_char = uuid.split('-')[2][0]
    assert version_char in '4', f"Incorrect version bit: {version_char}"
    
    # Check variant bit (in 3rd group)
    variant_char = uuid.split('-')[2][1]
    assert variant_char in '89ab', f"Incorrect variant bit: {variant_char}"

def test_uuid_length():
    """Ensure generated UUIDs have the correct total length."""
    uuid = generate_uuid()
    assert len(uuid) == 36, f"Incorrect UUID length: {len(uuid)}"