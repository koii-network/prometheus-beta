import re
import pytest
from src.uuid_generator import generate_uuid

def test_generate_uuid_returns_string():
    """Test that the function returns a string."""
    result = generate_uuid()
    assert isinstance(result, str), "Generated UUID should be a string"

def test_uuid_format():
    """Test that the generated UUID matches the standard UUID format."""
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    result = generate_uuid()
    assert re.match(uuid_pattern, result, re.IGNORECASE), "UUID does not match standard format"

def test_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuid_set = set(generate_uuid() for _ in range(1000))
    assert len(uuid_set) == 1000, "Generated UUIDs should be unique"

def test_uuid_length():
    """Test that the generated UUID has the correct length."""
    result = generate_uuid()
    assert len(result) == 36, "UUID should be 36 characters long"