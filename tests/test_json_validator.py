import pytest
from src.json_validator import is_valid_json

def test_valid_json_objects():
    """Test various valid JSON objects"""
    assert is_valid_json('{"name": "John", "age": 30}') == True
    assert is_valid_json('{"items": [1, 2, 3]}') == True
    assert is_valid_json('{"nested": {"key": "value"}}') == True

def test_invalid_json_strings():
    """Test various invalid JSON strings"""
    assert is_valid_json('{"missing": "quote}') == False
    assert is_valid_json('invalid json') == False
    assert is_valid_json('{key: "value"}') == False

def test_json_primitives():
    """Test JSON primitive types"""
    assert is_valid_json('"string"') == True
    assert is_valid_json('42') == True
    assert is_valid_json('true') == True
    assert is_valid_json('null') == True

def test_edge_cases():
    """Test edge case inputs"""
    assert is_valid_json('') == False
    assert is_valid_json(' ') == False
    assert is_valid_json(None) == False

def test_complex_json():
    """Test more complex JSON structures"""
    complex_json = '''
    {
        "name": "Complex Example",
        "numbers": [1, 2, 3],
        "nested": {
            "a": 1,
            "b": [true, false]
        },
        "nullable": null
    }
    '''
    assert is_valid_json(complex_json) == True