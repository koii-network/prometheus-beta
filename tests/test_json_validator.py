import pytest
from src.json_validator import is_valid_json

def test_valid_json_objects():
    # Test various valid JSON formats
    assert is_valid_json('{"key": "value"}') == True
    assert is_valid_json('{"numbers": [1, 2, 3]}') == True
    assert is_valid_json('{"nested": {"inner": "value"}}') == True
    assert is_valid_json('null') == True
    assert is_valid_json('true') == True
    assert is_valid_json('42') == True
    assert is_valid_json('[]') == True
    
def test_invalid_json():
    # Test various invalid JSON formats
    assert is_valid_json('') == False
    assert is_valid_json('{invalid json}') == False
    assert is_valid_json("{'single': 'quotes'}") == False  # Python dict, not JSON
    assert is_valid_json('{"unclosed": true') == False
    
def test_edge_cases():
    # Test edge cases and type handling
    assert is_valid_json(None) == False
    assert is_valid_json(123) == False
    assert is_valid_json([]) == False
    
def test_whitespace_json():
    # Test JSON with whitespace
    assert is_valid_json('  {"key": "value"}  ') == True
    assert is_valid_json('\n{"nested": {"key": "value"}}\n') == True