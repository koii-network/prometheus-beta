import re
import uuid

from src.uuid_generator import generate_uuid

def test_uuid_format():
    """Test that generated UUID matches the correct format."""
    generated_uuid = generate_uuid()
    
    # Check format using regex (8-4-4-4-12 hex characters)
    uuid_pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.IGNORECASE)
    assert uuid_pattern.match(generated_uuid), f"Invalid UUID format: {generated_uuid}"

def test_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuids = set()
    num_uuids = 1000
    
    for _ in range(num_uuids):
        uuids.add(generate_uuid())
    
    assert len(uuids) == num_uuids, "Generated UUIDs are not unique"

def test_uuid_version():
    """Verify that the UUID follows version 4 specification."""
    generated_uuid = generate_uuid()
    
    # Extract version (4th character in 3rd group)
    version_char = generated_uuid.split('-')[2][0]
    assert version_char == '4', f"UUID version is not 4, got {version_char}"

def test_uuid_variant():
    """Verify that the UUID follows the correct variant."""
    generated_uuid = generate_uuid()
    
    # Extract variant (first character of 4th group)
    variant_char = generated_uuid.split('-')[3][0]
    assert variant_char in ['8', '9', 'a', 'b'], f"Invalid UUID variant, got {variant_char}"

def test_uuid_length():
    """Verify the length of the generated UUID."""
    generated_uuid = generate_uuid()
    assert len(generated_uuid) == 36, f"Incorrect UUID length: {len(generated_uuid)}"