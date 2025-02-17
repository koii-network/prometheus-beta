import pytest
import re
from src.uuid_generator import generate_uuid

def test_generate_uuid_returns_string():
    """Test that the function returns a string."""
    uuid_value = generate_uuid()
    assert isinstance(uuid_value, str)

def test_generate_uuid_format():
    """Test that the generated UUID matches the standard UUID format."""
    uuid_value = generate_uuid()
    # UUID v4 format: 8-4-4-4-12 hexadecimal characters
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid_value, re.IGNORECASE) is not None

def test_generate_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuid1 = generate_uuid()
    uuid2 = generate_uuid()
    assert uuid1 != uuid2