import pytest
from src.json_parser import parse_api_response

def test_parse_valid_json():
    """Test parsing a valid JSON response."""
    valid_json = '{"name": "John", "age": 30}'
    result = parse_api_response(valid_json)
    assert result == {"name": "John", "age": 30}

def test_parse_nested_json():
    """Test parsing a nested JSON response."""
    nested_json = '{"user": {"name": "Jane", "details": {"city": "New York"}}}'
    result = parse_api_response(nested_json)
    assert result == {"user": {"name": "Jane", "details": {"city": "New York"}}}

def test_parse_invalid_json():
    """Test parsing an invalid JSON response."""
    invalid_json = '{invalid json}'
    result = parse_api_response(invalid_json)
    assert result is None

def test_parse_non_dictionary_json():
    """Test parsing a valid JSON that is not a dictionary."""
    list_json = '[1, 2, 3]'
    result = parse_api_response(list_json)
    assert result is None

def test_parse_empty_string():
    """Test parsing an empty string."""
    result = parse_api_response('')
    assert result is None