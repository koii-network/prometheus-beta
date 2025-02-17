import re
import pytest
from src.uuid_generator import generate_uuid

def test_generate_uuid_returns_string():
    """Test that the function returns a string."""
    result = generate_uuid()
    assert isinstance(result, str)

def test_generate_uuid_has_correct_format():
    """Test that the generated UUID matches the UUID v4 format."""
    result = generate_uuid()
    # UUID v4 regex pattern
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, result, re.IGNORECASE) is not None

def test_generate_uuid_is_unique():
    """Test that multiple generated UUIDs are different."""
    uuid1 = generate_uuid()
    uuid2 = generate_uuid()
    assert uuid1 != uuid2

def test_generate_uuid_total_length():
    """Test that the UUID has the correct total length."""
    result = generate_uuid()
    assert len(result) == 36  # 8-4-4-4-12 format with hyphens