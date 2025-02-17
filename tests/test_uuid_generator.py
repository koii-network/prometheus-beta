import re
import pytest
from src.uuid_generator import generate_uuid

def test_generate_uuid_returns_string():
    """Test that the function returns a string."""
    result = generate_uuid()
    assert isinstance(result, str)

def test_generate_uuid_format():
    """Test that the UUID matches the standard UUID format."""
    result = generate_uuid()
    uuid_pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
    assert uuid_pattern.match(result) is not None

def test_generate_uuid_unique():
    """Test that multiple generated UUIDs are unique."""
    uuid1 = generate_uuid()
    uuid2 = generate_uuid()
    assert uuid1 != uuid2