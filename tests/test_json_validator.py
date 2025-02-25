import pytest
from src.json_validator import is_valid_json

def test_valid_json_object():
    """Test validation of a valid JSON object."""
    assert is_valid_json('{"key": "value"}') == True

def test_valid_json_array():
    """Test validation of a valid JSON array."""
    assert is_valid_json('[1, 2, 3]') == True

def test_valid_json_nested():
    """Test validation of a nested valid JSON."""
    assert is_valid_json('{"key": {"nested": "value"}}') == True

def test_invalid_json_missing_quotes():
    """Test that JSON with missing quotes is considered invalid."""
    assert is_valid_json('{key: value}') == False

def test_invalid_json_syntax():
    """Test that JSON with invalid syntax is considered invalid."""
    assert is_valid_json('{invalid json}') == False

def test_empty_string():
    """Test that an empty string is not considered valid JSON."""
    assert is_valid_json('') == False

def test_whitespace_string():
    """Test that a whitespace-only string is not considered valid JSON."""
    assert is_valid_json('   ') == False

def test_none_input():
    """Test that None input is handled gracefully."""
    assert is_valid_json(None) == False

def test_number_input():
    """Test that non-string inputs are handled gracefully."""
    assert is_valid_json(123) == False