import pytest
from src.json_validator import is_valid_json

def test_valid_json_objects():
    # Test various valid JSON formats
    assert is_valid_json('{"key": "value"}') == True
    assert is_valid_json('{"num": 123}') == True
    assert is_valid_json('{"nested": {"inner": "value"}}') == True
    assert is_valid_json('[]') == True
    assert is_valid_json('{}') == True
    assert is_valid_json('[1, 2, 3]') == True
    assert is_valid_json('{"arr": [1, 2, 3]}') == True

def test_invalid_json():
    # Test various invalid JSON formats
    assert is_valid_json('') == False
    assert is_valid_json('Not JSON') == False
    assert is_valid_json('{broken json}') == False
    assert is_valid_json("{'single': 'quotes'}") == False  # Python dict, not JSON

def test_edge_cases():
    # Test edge cases and type handling
    assert is_valid_json(None) == False
    assert is_valid_json(123) == False
    assert is_valid_json(True) == False