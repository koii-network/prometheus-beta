import json
import pytest
from src.api_json_parser import parse_api_response

def test_parse_valid_json_string():
    """Test parsing a valid JSON string."""
    json_str = '{"key": "value", "number": 42}'
    result = parse_api_response(json_str)
    assert result == {"key": "value", "number": 42}

def test_parse_valid_json_bytes():
    """Test parsing a valid JSON byte string."""
    json_bytes = b'{"key": "value", "number": 42}'
    result = parse_api_response(json_bytes)
    assert result == {"key": "value", "number": 42}

def test_parse_already_parsed_dict():
    """Test passing an already parsed dictionary."""
    json_dict = {"key": "value", "number": 42}
    result = parse_api_response(json_dict)
    assert result == json_dict

def test_parse_empty_string():
    """Test parsing an empty string."""
    result = parse_api_response("")
    assert result is None

def test_parse_whitespace_string():
    """Test parsing a string with only whitespace."""
    result = parse_api_response("   \t\n")
    assert result is None

def test_parse_invalid_json():
    """Test parsing an invalid JSON string."""
    invalid_json = "{not a valid json}"
    result = parse_api_response(invalid_json)
    assert result is None

def test_parse_invalid_bytes():
    """Test parsing invalid bytes that can't be decoded."""
    invalid_bytes = b'\xff\xfe\xfd'  # Invalid UTF-8 bytes
    result = parse_api_response(invalid_bytes)
    assert result is None

def test_parse_unsupported_type():
    """Test that unsupported types raise a TypeError."""
    with pytest.raises(TypeError, match="Unsupported response type"):
        parse_api_response(12345)

def test_parse_nested_json():
    """Test parsing a nested JSON structure."""
    nested_json = '{"user": {"name": "John", "age": 30}, "active": true}'
    result = parse_api_response(nested_json)
    assert result == {"user": {"name": "John", "age": 30}, "active": True}

def test_parse_json_with_special_characters():
    """Test parsing JSON with special characters."""
    special_chars_json = '{"text": "Hello, World!", "symbols": "!@#$%^&*()_+"}'
    result = parse_api_response(special_chars_json)
    assert result == {"text": "Hello, World!", "symbols": "!@#$%^&*()_+"}