import re
import sys
import pytest
sys.path.append('.')

from src.uuid_generator import generate_uuid

def test_uuid_format():
    """Test that generated UUID matches the correct format."""
    uuid = generate_uuid()
    
    # Check UUID format using regex
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid), f"Invalid UUID format: {uuid}"

def test_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuids = set(generate_uuid() for _ in range(1000))
    assert len(uuids) == 1000, "Generated UUIDs are not unique"

def test_uuid_version():
    """Test that UUID starts with version 4."""
    uuid = generate_uuid()
    assert uuid[14] == '4', "UUID does not indicate version 4"

def test_uuid_variant():
    """Test that UUID has the correct variant bits."""
    uuid = generate_uuid()
    variant_char = uuid[19]
    assert variant_char in '89ab', "UUID does not have correct variant"

def test_uuid_length():
    """Test that generated UUID has the correct length."""
    uuid = generate_uuid()
    assert len(uuid) == 36, f"Incorrect UUID length: {len(uuid)}"