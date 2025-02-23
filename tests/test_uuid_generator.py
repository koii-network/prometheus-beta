import re
import pytest
from src.uuid_generator import generate_uuid

def test_generate_uuid_returns_string():
    """Test that the function returns a string."""
    result = generate_uuid()
    assert isinstance(result, str), "Should return a string"

def test_generate_uuid_format():
    """Test that the generated UUID matches the expected format."""
    result = generate_uuid()
    # UUID v4 format: 8-4-4-4-12 hexadecimal characters
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, result, re.IGNORECASE), "Should match UUID v4 format"

def test_generate_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuids = {generate_uuid() for _ in range(1000)}
    assert len(uuids) == 1000, "Generated UUIDs should be unique"