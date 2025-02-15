import pytest
import json
from src.api_response_parser import parse_json_response

def test_parse_valid_json():
    # Test parsing a simple valid JSON object
    test_response = '{"name": "John", "age": 30}'
    result = parse_json_response(test_response)
    assert result == {"name": "John", "age": 30}

def test_parse_nested_json():
    # Test parsing a nested JSON object
    test_response = '{"user": {"name": "Alice", "details": {"age": 25, "city": "New York"}}}'
    result = parse_json_response(test_response)
    assert result == {"user": {"name": "Alice", "details": {"age": 25, "city": "New York"}}}

def test_parse_json_array():
    # Test parsing a JSON array
    test_response = '["apple", "banana", "cherry"]'
    result = parse_json_response(test_response)
    assert result == ["apple", "banana", "cherry"]

def test_parse_invalid_json():
    # Test that an invalid JSON raises a ValueError
    invalid_json = '{"name": "John", "age": }'
    with pytest.raises(ValueError, match="Invalid JSON format"):
        parse_json_response(invalid_json)

def test_parse_empty_string():
    # Test parsing an empty string
    with pytest.raises(ValueError, match="Invalid JSON format"):
        parse_json_response("")

def test_parse_none():
    # Test parsing None input
    with pytest.raises(ValueError, match="Invalid JSON format"):
        parse_json_response(None)