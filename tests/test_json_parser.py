import pytest
from src.json_parser import parse_api_response

def test_parse_valid_json():
    """Test parsing a valid JSON response."""
    valid_json = '{"name": "John", "age": 30, "city": "New York"}'
    result = parse_api_response(valid_json)
    assert isinstance(result, dict)
    assert result == {"name": "John", "age": 30, "city": "New York"}

def test_parse_nested_json():
    """Test parsing a nested JSON response."""
    nested_json = '{"user": {"name": "Jane", "details": {"age": 25, "active": true}}}'
    result = parse_api_response(nested_json)
    assert isinstance(result, dict)
    assert result == {"user": {"name": "Jane", "details": {"age": 25, "active": True}}}

def test_parse_invalid_json():
    """Test parsing an invalid JSON string raises a ValueError."""
    invalid_json = '{"name": "John", "age": 30, "city": "New York"'  # Missing closing bracket
    with pytest.raises(ValueError, match="Invalid JSON string"):
        parse_api_response(invalid_json)

def test_parse_non_dict_json():
    """Test parsing a JSON that is not a dictionary raises a ValueError."""
    list_json = '[1, 2, 3]'
    with pytest.raises(ValueError, match="Parsed JSON must be a dictionary"):
        parse_api_response(list_json)

def test_parse_empty_string():
    """Test parsing an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid JSON string"):
        parse_api_response("")

def test_parse_none():
    """Test parsing None raises a ValueError."""
    with pytest.raises(ValueError):
        parse_api_response(None)  # type: ignore