import pytest
import json
from src.api_json_parser import parse_api_response

def test_parse_valid_json():
    """Test parsing a valid JSON response."""
    test_json = '{"name": "John", "age": 30}'
    result = parse_api_response(test_json)
    assert result == {"name": "John", "age": 30}

def test_parse_nested_json():
    """Test parsing a nested JSON response."""
    test_json = '{"user": {"name": "Alice", "details": {"age": 25, "city": "New York"}}}'
    result = parse_api_response(test_json)
    assert result == {"user": {"name": "Alice", "details": {"age": 25, "city": "New York"}}}

def test_parse_invalid_json():
    """Test that an invalid JSON raises a ValueError."""
    invalid_json = '{"name": "John", "age": 30'  # Missing closing brace
    with pytest.raises(ValueError, match="Invalid JSON format"):
        parse_api_response(invalid_json)

def test_parse_empty_input():
    """Test that empty input returns None."""
    result = parse_api_response("")
    assert result is None

def test_parse_non_string_input():
    """Test that non-string input returns None."""
    result = parse_api_response(123)
    assert result is None