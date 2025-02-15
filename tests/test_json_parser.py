import pytest
import json
from src.json_parser import parse_api_response

def test_parse_valid_json():
    """Test parsing a valid JSON response"""
    test_json = '{"name": "John", "age": 30, "city": "New York"}'
    result = parse_api_response(test_json)
    assert result is not None
    assert result['name'] == 'John'
    assert result['age'] == 30
    assert result['city'] == 'New York'

def test_parse_nested_json():
    """Test parsing a nested JSON response"""
    test_json = '{"user": {"name": "Jane", "details": {"age": 25, "country": "Canada"}}}'
    result = parse_api_response(test_json)
    assert result is not None
    assert result['user']['name'] == 'Jane'
    assert result['user']['details']['age'] == 25

def test_parse_empty_json():
    """Test parsing an empty JSON object"""
    test_json = '{}'
    result = parse_api_response(test_json)
    assert result == {}

def test_parse_invalid_json():
    """Test parsing an invalid JSON string"""
    invalid_json = 'This is not a JSON string'
    result = parse_api_response(invalid_json)
    assert result is None

def test_parse_json_with_special_characters():
    """Test parsing JSON with special characters"""
    test_json = '{"message": "Hello, world!", "special_chars": "!@#$%^&*()"}'
    result = parse_api_response(test_json)
    assert result is not None
    assert result['message'] == 'Hello, world!'
    assert result['special_chars'] == '!@#$%^&*()'