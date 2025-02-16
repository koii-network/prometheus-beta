import re
import sys
import pytest
sys.path.append('src')

from uuid_generator import generate_uuid

def test_generate_uuid_format():
    """Test that the generated UUID matches the correct format."""
    uuid = generate_uuid()
    
    # Regex pattern for UUID v4
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    
    assert re.match(uuid_pattern, uuid, re.IGNORECASE), f"Invalid UUID format: {uuid}"

def test_generate_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuids = set()
    num_uuids = 1000
    
    for _ in range(num_uuids):
        uuids.add(generate_uuid())
    
    assert len(uuids) == num_uuids, "Generated UUIDs are not unique"

def test_generate_uuid_version():
    """Test that the UUID version is correctly set to 4."""
    uuid = generate_uuid()
    
    # Check the version bit (4th character of the 3rd segment should be '4')
    segments = uuid.split('-')
    assert segments[2][0] == '4', f"Incorrect UUID version in {uuid}"

def test_generate_uuid_variant():
    """Test that the UUID variant bits are correctly set."""
    uuid = generate_uuid()
    
    # Check the variant bits (first character of the 4th segment should be 8, 9, a, or b)
    segments = uuid.split('-')
    variant_char = segments[3][0]
    assert variant_char in '89ab', f"Incorrect UUID variant in {uuid}"