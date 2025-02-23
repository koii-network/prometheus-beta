import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_format():
    """Test that the generated UUID matches the standard format."""
    uuid = generate_uuid()
    
    # Check overall UUID format
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid), f"UUID {uuid} does not match the expected format"

def test_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuids = set()
    num_generations = 1000
    
    for _ in range(num_generations):
        uuids.add(generate_uuid())
    
    assert len(uuids) == num_generations, "UUIDs are not unique"

def test_uuid_version():
    """Test that the UUID version is correctly set to 4."""
    uuid = generate_uuid()
    version_char = uuid.split('-')[2][0]
    assert version_char == '4', f"UUID version is incorrect: {version_char}"

def test_uuid_variant():
    """Test that the UUID variant is correctly set."""
    uuid = generate_uuid()
    variant_char = uuid.split('-')[3][0]
    assert variant_char in '89ab', f"UUID variant is incorrect: {variant_char}"

def test_generate_multiple_uuids():
    """Ensure multiple UUID generations work correctly."""
    uuid1 = generate_uuid()
    uuid2 = generate_uuid()
    
    assert uuid1 != uuid2, "Multiple UUID generations produced the same UUID"